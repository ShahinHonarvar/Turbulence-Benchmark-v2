def all_left_right_truncatable_prime(numbers):
    x = numbers[94]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for num in range(2, x + 1):
        num_str = str(num)
        if '0' not in num_str and is_prime(num):
            truncatable = True
            for i in range(1, len(num_str)):
                if not (is_prime(int(num_str[i:])) and is_prime(int(num_str[:-i]))):
                    truncatable = False
                    break
            if truncatable:
                primes.append(num)
    return sorted(primes)