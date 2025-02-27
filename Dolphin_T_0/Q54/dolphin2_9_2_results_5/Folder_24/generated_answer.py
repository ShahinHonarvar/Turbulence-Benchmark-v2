def all_right_truncatable_prime(tuple_of_positive_integers):

    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0 or n == 1:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        str_n = str(n)
        for i in range(len(str_n) - 1, 0, -1):
            if not is_prime(int(str_n[i:])):
                return False
        return True
    x = tuple_of_positive_integers[65]
    right_truncatable_prime_list = [i for i in range(2, x) if is_right_truncatable_prime(i)]
    return sorted(right_truncatable_prime_list, reverse=True)