def all_left_right_truncatable_prime(n):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(num):
        if not is_prime(num):
            return False
        if '0' in str(num):
            return False
        s = str(num)
        return all((is_prime(int(s[i:])) and is_prime(int(s[:i])) for i in range(1, len(s))))
    x = n[65]
    return sorted([i for i in range(2, x + 1) if is_left_right_truncatable_prime(i)], reverse=True)