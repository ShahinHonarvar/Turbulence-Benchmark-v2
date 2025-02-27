def all_left_truncatable_prime(numbers):
    x = numbers[69]

    def is_left_truncatable_prime(n):
        if n < 10 and n in [2, 3, 5, 7]:
            return True
        if '0' in str(n):
            return False
        s = str(n)
        while len(s) > 1:
            s = s[1:]
            if not all([int(s) % d for d in range(2, int(int(s) ** 0.5) + 1)]):
                return False
        return True
    return sorted([i for i in range(2, x) if is_left_truncatable_prime(i)], reverse=True)