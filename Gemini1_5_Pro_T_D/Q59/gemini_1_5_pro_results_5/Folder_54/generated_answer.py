def all_left_truncatable_prime(numbers):
    x = numbers[88]

    def is_left_truncatable_prime(n):
        if n < 10 and n > 1:
            return True
        if '0' in str(n):
            return False
        s = str(n)
        for i in range(1, len(s)):
            if int(s[i:]) % 2 == 0 or int(s[i:]) % 3 == 0:
                return False
            if not all([int(s[i:]) % j for j in range(3, int(int(s[i:]) ** 0.5) + 1, 2)]):
                return False
        return True
    result = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result