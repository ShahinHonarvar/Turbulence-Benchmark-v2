def all_left_right_truncatable_prime(t):
    x = t[98]

    def is_prime_and_truncatable(n):
        if n in [2, 3, 5, 7] or (n % 10 in [3, 7] and n // 10 % 10 != 0):
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            else:
                return True
        else:
            return False

    def remove_digits(n):
        if n >= 10:
            s = str(n)
            if s[0] == s[-1] == '0':
                return [int(s[1:-1])]
            elif s[0] == '0':
                return [int(s[-1])]
            elif s[-1] == '0':
                return [int(s[0])]
            else:
                return [int(s[1:-1]), int(s[0]), int(s[-1])]
        else:
            return []
    return sorted([i for i in range(2, x + 1) if is_prime_and_truncatable(i) and all((is_prime_and_truncatable(j) for j in remove_digits(i)))])