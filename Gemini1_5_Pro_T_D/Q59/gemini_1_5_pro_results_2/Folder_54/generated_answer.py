def all_left_truncatable_prime(numbers):
    x = numbers[88]

    def is_left_truncatable_prime(n):
        if n < 10 or '0' in str(n):
            return False
        s = str(n)
        while s:
            if int(s) == 1:
                return False
            if not all([int(s) % i for i in range(2, int(int(s) ** 0.5) + 1)]).count(0) == 0:
                return False
            s = s[1:]
        return True
    return sorted([i for i in range(2, x) if is_left_truncatable_prime(i)], reverse=True)