def all_left_truncatable_prime(integers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_left_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        while n > 0:
            if not is_prime(n):
                return False
            str_n = str_n[1:]
            n = int(str_n) if str_n else 0
        return True
    x = integers[6]
    result = [n for n in range(2, x) if is_left_truncatable_prime(n)]
    return sorted(result, reverse=True)