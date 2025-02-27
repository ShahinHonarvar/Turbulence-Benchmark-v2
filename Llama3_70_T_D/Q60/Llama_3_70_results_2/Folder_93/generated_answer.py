def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[11]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    left_right_truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        if '0' in str_prime:
            continue
        is_left_right_truncatable = True
        for i in range(1, len(str_prime)):
            if not is_prime(int(str_prime[i:])) or not is_prime(int(str_prime[:-i])):
                is_left_right_truncatable = False
                break
        if is_left_right_truncatable:
            left_right_truncatable_primes.append(prime)
    return sorted(left_right_truncatable_primes)