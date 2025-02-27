def all_left_right_truncatable_prime(numbers):
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def is_left_right_truncatable(n):
        string_n = str(n)
        if '0' in string_n:
            return False
        for i in range(len(string_n) - 1):
            if not is_prime(int(string_n[i + 1:])) or not is_prime(int(string_n[:i + 1])):
                return False
        return True
    x = numbers[41]
    for number in range(x, 1, -1):
        if is_prime(number) and is_left_right_truncatable(number):
            primes.append(number)
    return primes