def all_left_truncatable_prime(numbers):
    x = numbers[31]

    def is_left_truncatable_prime(n):
        if n < 10 and n in (2, 3, 5, 7):
            return True
        if '0' in str(n) or n < 2:
            return False
        s = str(n)
        for i in range(len(s)):
            if int(s[i:]) not in (2, 3, 5, 7) and (not (int(s[i:]) > 7 and all((int(s[i:]) % j for j in (2, 3, 5, 7))))):
                return False
        return True
    result = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result