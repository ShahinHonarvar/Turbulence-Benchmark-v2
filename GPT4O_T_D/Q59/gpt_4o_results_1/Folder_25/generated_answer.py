def all_left_truncatable_prime(numbers):
    if len(numbers) <= 92:
        return []
    x = numbers[92]

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        s = str(num)
        while s:
            if '0' in s or not is_prime(int(s)):
                return False
            s = s[1:]
        return True
    result = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            result.append(i)
    return sorted(result)