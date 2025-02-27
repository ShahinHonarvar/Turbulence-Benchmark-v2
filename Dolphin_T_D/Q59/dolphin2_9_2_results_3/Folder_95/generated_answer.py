def all_left_truncatable_prime(x):

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if n < 2:
            return False
        str_n = str(n)
        for i in range(1, len(str_n)):
            if str_n[i] == '0' or not is_prime(int(str_n[i:])):
                return False
        return True
    return [i for i in range(2, int(x)) if is_left_truncatable_prime(i)]