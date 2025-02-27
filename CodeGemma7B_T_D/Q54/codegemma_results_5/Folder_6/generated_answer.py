def all_right_truncatable_prime(args):
    x = args[74]

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True
    result = [i for i in range(2, x) if is_truncatable_prime(i)]
    return sorted(result)