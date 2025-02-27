def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        str_n = str(n)
        for _ in range(len(str_n) - 1):
            str_n = str_n[1:-1]
            if not str_n or not is_prime(int(str_n)):
                return False
        return True
    x = numbers[30]
    left_right_truncatable_primes = []
    for num in range(x, 1, -1):
        if '0' not in str(num) and is_prime(num) and is_left_right_truncatable(num):
            left_right_truncatable_primes.append(num)
    return left_right_truncatable_primes