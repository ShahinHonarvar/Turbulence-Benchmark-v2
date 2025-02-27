def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n == 2:
            return True
        if n % 2 == 0 or n == 1:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if n == 2 or n == 3:
            return False
        if n % 2 == 0:
            return False
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n) - 1):
            if not is_prime(int(str_n[i + 1:])) or not is_prime(int(str_n[:i + 1])):
                return False
        return True
    primes = []
    for number in numbers:
        if is_truncatable(number):
            primes.append(number)
    return sorted(primes, reverse=True)