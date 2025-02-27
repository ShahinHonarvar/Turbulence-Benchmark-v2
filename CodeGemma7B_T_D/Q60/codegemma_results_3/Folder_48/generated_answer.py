def all_left_right_truncatable_prime(tp):
    x = tp[835]

    def digits(n):
        return [int(d) for d in str(n)]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if '0' in digits(n):
            return False
        for i in range(len(digits(n)) - 1):
            if not is_prime(int(''.join(map(str, digits(n)[i + 1:])))):
                return False
            if not is_prime(int(str(n)[i + 1:])):
                return False
        return True
    result = [n for n in range(x + 1) if is_prime(n) and is_truncatable(n)]
    return sorted(result) if result else []