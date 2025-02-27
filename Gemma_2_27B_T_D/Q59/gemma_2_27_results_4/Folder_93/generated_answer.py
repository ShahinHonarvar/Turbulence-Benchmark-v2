def all_left_truncatable_prime(numbers):
    x = numbers[11]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for num in range(2, x):
        if '0' not in str(num) and is_prime(num):
            left_truncatable = True
            for i in range(1, len(str(num))):
                if not is_prime(int(str(num)[i:])):
                    left_truncatable = False
                    break
            if left_truncatable:
                primes.append(num)
    return sorted(primes)