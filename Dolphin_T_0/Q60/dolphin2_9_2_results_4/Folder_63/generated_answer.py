def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0 or n == 1:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        n = str(n)
        for i in range(len(n) - 1):
            if not is_prime(int(n[i + 1:])) or not is_prime(int(n[:i + 1])):
                return False
        return n
    primes = [i for i in range(2, numbers[88] + 1) if is_prime(i)]
    lr = [i for i in primes if is_truncatable_prime(i)]
    return sorted(lr)