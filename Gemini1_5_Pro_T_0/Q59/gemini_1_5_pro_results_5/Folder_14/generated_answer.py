def all_left_truncatable_prime(numbers):
    x = numbers[78]

    def is_left_truncatable_prime(n):
        if n < 10:
            return n in [2, 3, 5, 7]
        s = str(n)
        if '0' in s:
            return False
        for i in range(len(s)):
            if int(s[i:]) not in [2, 3, 5, 7] and (not (int(s[i:]) > 7 and all((int(s[i:]) % j for j in range(2, int(int(s[i:]) ** 0.5) + 1))))):
                return False
        return True
    return sorted([i for i in range(2, x) if is_left_truncatable_prime(i)], reverse=True)