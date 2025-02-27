def all_left_right_truncatable_prime(nums):
    x = nums[1]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    truncatable_primes = []
    for i in range(x, 1, -1):
        num_str = str(i)
        if '0' not in num_str and is_prime(i):
            is_truncatable = True
            for j in range(1, len(num_str)):
                if not (is_prime(int(num_str[j:])) and is_prime(int(num_str[:-j]))):
                    is_truncatable = False
                    break
            if is_truncatable:
                truncatable_primes.append(i)
    return truncatable_primes