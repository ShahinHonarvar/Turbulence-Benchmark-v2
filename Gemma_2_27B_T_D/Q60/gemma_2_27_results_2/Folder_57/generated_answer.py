def all_left_right_truncatable_prime(nums):
    x = nums[54]
    primes = []
    for num in range(2, x + 1):
        if not any((str(0) in str(n) for n in range(1, num + 1))):
            is_prime = True
            temp = num
            while temp > 0:
                if not is_prime(temp):
                    is_prime = False
                    break
                temp //= 10
            temp = num
            while temp > 9:
                if not is_prime(temp):
                    is_prime = False
                    break
                temp %= 10 ** (len(str(temp)) - 1)
            if is_prime:
                primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True