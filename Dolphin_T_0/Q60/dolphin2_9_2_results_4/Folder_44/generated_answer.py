def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_left_right_truncatable_prime(nums):
    nums = sorted(list(filter(lambda num: is_prime(num), nums)))
    x = nums[-1]
    primes = []
    for i in range(2, x + 1):
        if is_prime(i):
            digits = [int(d) for d in str(i)]
            while digits:
                if digits[0] == 0 or digits[-1] == 0:
                    break
                if is_prime(int(''.join(map(str, digits[1:-1])))):
                    primes.append(i)
                    break
                digits = digits[1:-1]
    return primes