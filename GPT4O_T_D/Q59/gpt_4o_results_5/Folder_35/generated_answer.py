def all_left_truncatable_prime(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable(num):
        s = str(num)
        while s:
            if not is_prime(int(s)):
                return False
            s = s[1:]
        return True
    x = numbers[177]
    result = []
    for num in range(2, x):
        if '0' not in str(num) and is_left_truncatable(num):
            result.append(num)
    return sorted(result)