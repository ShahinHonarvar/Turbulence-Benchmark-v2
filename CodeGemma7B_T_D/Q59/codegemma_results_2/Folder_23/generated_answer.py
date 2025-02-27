def all_left_truncatable_prime(tuple_of_positive_int):
    x = tuple_of_positive_int[76]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True
    result = [a for a in range(x) if is_left_truncatable_prime(a)]
    result.sort(reverse=True)
    return result