def all_right_truncatable_prime(numbers):
    x = numbers[630]

    def is_right_truncatable_prime(n):
        if n <= 1:
            return False
        s = str(n)
        for i in range(len(s)):
            if int(s[i:]) <= 1:
                return False
            if not all([int(s[i:]) % j for j in range(2, int(int(s[i:]) ** 0.5) + 1)]):
                return False
        return True
    result = sorted([i for i in range(2, x) if is_right_truncatable_prime(i)], reverse=True)
    return result