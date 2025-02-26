def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums_tuple):
    x = nums_tuple[38]
    left_truncatable_primes = []
    for n in range(x - 1, 1, -1):
        if '0' not in str(n):
            is_truncatable = True
            num_str = str(n)
            for i in range(1, len(num_str)):
                if not is_prime(int(num_str[i:])):
                    is_truncatable = False
                    break
            if is_truncatable and is_prime(n):
                left_truncatable_primes.append(n)
    return sorted(left_truncatable_primes, reverse=True)