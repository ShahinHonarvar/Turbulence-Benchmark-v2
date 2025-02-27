def all_left_truncatable_prime(numbers):
    x = numbers[22]

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        num_str = str(num)
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])):
                return False
        return True
    truncatable_primes = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)