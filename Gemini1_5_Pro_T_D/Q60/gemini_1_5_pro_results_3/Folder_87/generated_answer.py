def all_left_right_truncatable_prime(numbers):
    x = numbers[39]

    def is_truncatable_prime(num):
        if num <= 1 or '0' in str(num):
            return False
        if num in [2, 3, 5, 7]:
            return True
        s = str(num)
        for i in range(1, len(s)):
            if not (int(s[i:]) in [2, 3, 5, 7] or (int(s[i:]) > 7 and all((int(s[i:]) % j for j in range(3, int(int(s[i:]) ** 0.5) + 1, 2))))):
                return False
            if not (int(s[:-i]) in [2, 3, 5, 7] or (int(s[:-i]) > 7 and all((int(s[:-i]) % j for j in range(3, int(int(s[:-i]) ** 0.5) + 1, 2))))):
                return False
        return True
    result = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result