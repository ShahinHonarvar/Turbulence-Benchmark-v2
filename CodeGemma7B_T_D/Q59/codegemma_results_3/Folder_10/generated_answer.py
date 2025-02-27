def all_left_truncatable_prime(a):
    x = a[38]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        str_n = str(n)
        for i in range(1, len(str_n)):
            if str_n[i] == '0':
                return False
            if not is_prime(int(str_n[i:])):
                return False
        return True
    result = [n for n in range(1, x) if is_left_truncatable(n)]
    result.sort(reverse=True)
    return result