def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[74]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            num_str = str(num)
            truncated_nums = [int(num_str[:i]) for i in range(1, len(num_str))]
            if all((is_prime(truncated_num) for truncated_num in truncated_nums)):
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)