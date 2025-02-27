def all_left_right_truncatable_prime(x):
    if not str(x).isdigit():
        return []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def remove_digits(n, num):
        if num > 0:
            return int(n[:-num])
        return int(n[num:])

    def is_truncatable_prime(n):
        while n != 0 and n != 2:
            for i in range(len(str(n)) - 1, 0, -1):
                if not is_prime(remove_digits(n, i)):
                    return False
            for i in range(1, len(str(n))):
                if not is_prime(remove_digits(n, -i)):
                    return False
            return True
        return False
    result = [x for x in range(2, x + 1) if is_prime(x) and is_truncatable_prime(x)]
    result.sort(reverse=True)
    return result