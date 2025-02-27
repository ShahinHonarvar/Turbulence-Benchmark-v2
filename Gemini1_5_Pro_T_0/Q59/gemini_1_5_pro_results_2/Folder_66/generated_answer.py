def all_left_truncatable_prime(numbers):
    x = numbers[25]

    def is_left_truncatable_prime(n):
        if n < 10 and n > 0:
            return True if n in {2, 3, 5, 7} else False
        if '0' in str(n):
            return False
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        s = str(n)
        for i in range(1, len(s)):
            if int(s[i:]) % 2 == 0 or int(s[i:]) < 2:
                return False
            for j in range(3, int(int(s[i:]) ** 0.5) + 1, 2):
                if int(s[i:]) % j == 0:
                    return False
        return True
    result = []
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            result.append(num)
    result.sort(reverse=True)
    return result