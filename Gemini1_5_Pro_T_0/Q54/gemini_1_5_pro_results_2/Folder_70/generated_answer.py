def all_right_truncatable_prime(numbers):
    x = numbers[433]

    def is_right_truncatable_prime(n):
        if n < 10 and n != 2 and (n != 3) and (n != 5) and (n != 7):
            return False
        s = str(n)
        for i in range(len(s)):
            if int(s[i:]) % 2 == 0 or int(s[i:]) % 3 == 0 or int(s[i:]) % 5 == 0 or (int(s[i:]) == 1):
                return False
            for j in range(2, int(int(s[i:]) ** 0.5) + 1):
                if int(s[i:]) % j == 0:
                    return False
        return True
    result = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result