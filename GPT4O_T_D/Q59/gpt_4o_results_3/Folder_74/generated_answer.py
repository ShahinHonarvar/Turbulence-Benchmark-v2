def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(p):
        str_p = str(p)
        if '0' in str_p:
            return False
        for i in range(len(str_p)):
            if not is_prime(int(str_p[i:])):
                return False
        return True
    x = numbers[36]
    return sorted([n for n in range(2, x) if is_left_truncatable_prime(n)])