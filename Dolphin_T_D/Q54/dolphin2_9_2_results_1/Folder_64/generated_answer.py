def all_right_truncatable_prime(input_tuple):

    def is_right_truncatable_prime(n, x):
        for i in range(len(str(n)) - 1, 0, -1):
            if int(n[i:]) >= x:
                break
            if not is_prime(int(n[i:])):
                return False
        return True

    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = input_tuple[4]
    result = [i for i in range(x - 1) if is_right_truncatable_prime(str(i), x)]
    return result