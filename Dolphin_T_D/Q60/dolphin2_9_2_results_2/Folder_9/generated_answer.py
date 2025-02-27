def all_left_right_truncatable_prime(numbers):
    x = numbers[29]
    primes = [2]

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_trunc(n):
        while len(str(n)) > 1:
            if not is_prime(n):
                return False
            n = n // 10
            if not is_prime(n):
                return False
            n = n % 10
        return True
    result = [i for i in primes if i <= x and is_trunc(i)]
    result.sort(reverse=True)
    return result