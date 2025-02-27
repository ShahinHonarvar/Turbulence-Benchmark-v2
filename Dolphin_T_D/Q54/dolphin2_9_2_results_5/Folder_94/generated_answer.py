def all_right_truncatable_prime(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    x = numbers[43]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            truncation = num
            while truncation > 1:
                truncation //= 10
                if not is_prime(truncation):
                    break
            else:
                primes.append(num)
    return sorted(primes)