def all_left_truncatable_prime(numbers):
    x = numbers[767]

    def is_left_truncatable_prime(num):
        if num < 10 and num > 1:
            return True
        if '0' in str(num) or num < 1:
            return False
        s = str(num)
        for i in range(1, len(s)):
            if int(s[i:]) % 2 == 0 or int(s[i:]) % 3 == 0:
                return False
            if not is_prime(int(s[i:])):
                return False
        return True

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    result = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result