def all_left_truncatable_prime(numbers):
    x = numbers[96]

    def is_left_truncatable_prime(num):
        if num < 10 and num > 1:
            return True
        if '0' in str(num):
            return False
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        s = str(num)
        while len(s) > 1:
            s = s[1:]
            if not is_left_truncatable_prime(int(s)):
                return False
        return True
    result = []
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            result.append(num)
    result.sort(reverse=True)
    return result