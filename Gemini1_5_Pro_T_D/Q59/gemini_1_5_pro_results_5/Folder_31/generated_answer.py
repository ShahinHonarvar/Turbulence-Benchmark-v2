def all_left_truncatable_prime(numbers):
    x = numbers[50]

    def is_left_truncatable_prime(n):
        if n < 10 and n > 0:
            return n > 1
        if '0' in str(n):
            return False
        s = str(n)
        for i in range(1, len(s)):
            if int(s[i:]) % 2 == 0 or int(s[i:]) % 3 == 0:
                return False
            if not is_prime(int(s[i:])):
                return False
        return is_prime(n)

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