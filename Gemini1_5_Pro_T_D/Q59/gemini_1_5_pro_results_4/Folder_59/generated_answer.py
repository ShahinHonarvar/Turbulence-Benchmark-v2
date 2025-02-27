def all_left_truncatable_prime(numbers):
    x = numbers[84]

    def is_left_truncatable_prime(n):
        if n < 10 and n in {2, 3, 5, 7}:
            return True
        if '0' in str(n) or n < 10:
            return False
        s = str(n)
        for i in range(1, len(s)):
            if int(s[i:]) not in {2, 3, 5, 7} and (not (int(s[i:]) > 7 and all((int(s[i:]) % j for j in range(2, int(int(s[i:]) ** 0.5) + 1))))):
                return False
        return True
    return sorted([i for i in range(2, x) if is_left_truncatable_prime(i)], reverse=True)