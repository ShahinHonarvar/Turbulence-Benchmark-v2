def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[85]
    primes = []
    for i in range(2, x + 1):
        if '0' not in str(i) and is_prime(i):
            while i != 0:
                i = i // 10
                if is_prime(i):
                    last_digit = i % 10
                    i //= 10
                    if is_prime(i) and last_digit != 0:
                        primes.append(i)
    return sorted(list(set(primes)))