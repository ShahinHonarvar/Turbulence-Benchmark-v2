def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        n = str(n)
        for i in range(len(n)):
            if n[i] == '0':
                return False
            if not is_prime(int(n[i:])):
                return False
            if i != 0 and (not is_prime(int(n[:i]))):
                return False
        return True
    return [i for i in range(2, x + 1) if is_truncatable_prime(i)]