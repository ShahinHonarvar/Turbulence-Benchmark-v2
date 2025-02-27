def all_left_right_truncatable_prime(numbers_tuple):

    def check_trunc(n):
        return all((int(str(n)[i:j]) for i in range(len(str(n))) for j in range(i + 1, len(str(n)) + 1)))

    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0 or n == 1:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    x = numbers_tuple[52]
    primes = [i for i in range(2, x) if is_prime(i)]
    return sorted([i for i in primes if check_trunc(i)], reverse=True)