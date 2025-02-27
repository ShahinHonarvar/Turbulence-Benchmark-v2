def all_left_truncatable_prime(nums):

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = nums[466]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        if is_prime(num):
            truncated_forms = []
            for i in range(1, len(str(num))):
                truncated_forms.append(int(str(num)[:i]))
            if all((is_prime(n) for n in truncated_forms)):
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)