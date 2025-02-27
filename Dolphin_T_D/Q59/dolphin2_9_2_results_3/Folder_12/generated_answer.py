def all_left_truncatable_prime(numbers: tuple) -> list:

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def remove_digit(n):
        s = str(n)
        return int(s[1:])

    def left_truncatable_prime(n):
        i = n
        while i != 0:
            if not is_prime(i):
                return False
            i = remove_digit(i)
        return True
    x = numbers[70]
    primes = [i for i in range(x, 0, -1) if left_truncatable_prime(i) and i > 9]
    return primes