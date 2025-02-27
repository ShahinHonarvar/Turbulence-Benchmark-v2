def all_right_truncatable_prime(numbers):
    x = numbers[61]

    def is_right_truncatable_prime(n):
        if n < 2:
            return False
        s = str(n)
        for i in range(len(s)):
            if int(s[i:]) < 2:
                return False
            if not all([int(s[i:]) % j for j in range(2, int(int(s[i:]) ** 0.5) + 1)]):
                return False
        return True
    result = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            result.append(i)
    return sorted(result)