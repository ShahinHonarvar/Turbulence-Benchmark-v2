def all_left_right_truncatable_prime(numbers):
    x = numbers[54]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        str_n = str(n)
        for i in range(len(str_n)):
            if str_n[i] == '0':
                return False
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:len(str_n) - i])):
                return False
        return True
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            primes.append(num)
    return primes