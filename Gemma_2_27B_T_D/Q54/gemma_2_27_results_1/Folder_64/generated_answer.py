def all_right_truncatable_prime(numbers):
    x = numbers[4]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            temp = str(i)
            is_truncatable = True
            for j in range(len(temp) - 1, 0, -1):
                if not is_prime(int(temp[:j])):
                    is_truncatable = False
                    break
            if is_truncatable:
                truncatable_primes.append(i)
    return sorted(truncatable_primes)