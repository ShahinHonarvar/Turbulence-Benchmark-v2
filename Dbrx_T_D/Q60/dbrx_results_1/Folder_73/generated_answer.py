from sympy import isprime

def all_left_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[97]
    result = []

    def is_prime(n):
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        if n < 10:
            return is_prime(n)
        if '0' in str(n):
            return False
        return is_prime(n) and is_left_right_truncatable(int(str(n)[1:])) and is_left_right_truncatable(int(str(n)[:-1]))
    for i in range(2, x + 1):
        if is_left_right_truncatable(i):
            result.append(i)
    return sorted(result)