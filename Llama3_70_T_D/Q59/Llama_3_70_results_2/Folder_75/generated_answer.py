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

def all_left_truncatable_prime(nums):
    x = nums[41]
    left_truncatable_primes = []
    for i in range(2, x):
        if str(i)[0] == '0':
            continue
        if is_prime(i):
            j = i
            prime = True
            while j > 9:
                j = int(str(j)[1:])
                if not is_prime(j):
                    prime = False
                    break
            if prime:
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)