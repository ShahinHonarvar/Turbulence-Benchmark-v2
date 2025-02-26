def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[945]
    left_truncatable_primes = []
    for n in range(x):
        if n < 10:
            if is_prime(n):
                left_truncatable_primes.append(n)
        else:
            str_n = str(n)
            if '0' not in str_n:
                is_truncatable = True
                for i in range(len(str_n)):
                    truncated = int(str_n[i:])
                    if not is_prime(truncated):
                        is_truncatable = False
                        break
                if is_truncatable:
                    left_truncatable_primes.append(n)
    return sorted(left_truncatable_primes, reverse=True)