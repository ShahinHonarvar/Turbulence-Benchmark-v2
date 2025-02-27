def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[29]
    right_truncatable_primes = []
    for num in range(2, x):
        num_str = str(num)
        all_truncations_prime = True
        for i in range(len(num_str)):
            truncation = int(num_str[:-i or len(num_str)])
            if not is_prime(truncation):
                all_truncations_prime = False
                break
        if all_truncations_prime and is_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)