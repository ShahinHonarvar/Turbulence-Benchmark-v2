def all_right_truncatable_prime(numbers):
    x = numbers[758]

    def is_right_truncatable_prime(n):
        if n < 2:
            return False
        s = str(n)
        for i in range(len(s)):
            if int(s[i:]) % 2 == 0 or int(s[i:]) == 1:
                return False
            for j in range(3, int(int(s[i:]) ** 0.5) + 1, 2):
                if int(s[i:]) % j == 0:
                    return False
        return True
    result = sorted([i for i in range(2, x) if is_right_truncatable_prime(i)])
    return result