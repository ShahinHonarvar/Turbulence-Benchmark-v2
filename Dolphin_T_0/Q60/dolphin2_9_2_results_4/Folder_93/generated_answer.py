def all_left_right_truncatable_prime(numbers):

    def check_truncatable(n):
        n_str = str(n)
        for _ in range(len(n_str) - 1):
            n_str = n_str[1:-1]
            if not is_prime(int(n_str)):
                return False
        return True

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i ** 2 <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    x = numbers[11]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    return [i for i in primes if check_truncatable(i)]