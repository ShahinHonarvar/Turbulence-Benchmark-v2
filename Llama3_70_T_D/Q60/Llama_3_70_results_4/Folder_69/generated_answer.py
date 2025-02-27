def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[760]

    def is_left_right_truncatable_prime(n):
        n_str = str(n)
        if '0' in n_str:
            return False
        for i in range(1, len(n_str)):
            if not is_prime(int(n_str[i:])) or not is_prime(int(n_str[:-i])):
                return False
        return is_prime(n)
    truncatable_primes = [i for i in range(2, x + 1) if is_left_right_truncatable_prime(i)]
    truncatable_primes.sort(reverse=True)
    return truncatable_primes