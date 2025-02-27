def all_right_truncatable_prime(numbers):
    x = numbers[20]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for num in range(x, 1, -1):
        if is_prime(num):
            is_truncatable = True
            num_str = str(num)
            for i in range(1, len(num_str)):
                if not is_prime(int(num_str[:-i])):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(num)
    return sorted(primes, reverse=True)