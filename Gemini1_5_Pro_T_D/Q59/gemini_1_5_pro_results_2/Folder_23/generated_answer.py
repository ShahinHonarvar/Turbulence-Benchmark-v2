def all_left_truncatable_prime(numbers):
    x = numbers[77]

    def is_left_truncatable_prime(num):
        if num < 10 and num > 1:
            return True
        if '0' in str(num) or num < 10:
            return False
        s = str(num)
        for i in range(1, len(s)):
            if int(s[i:]) % 2 == 0:
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