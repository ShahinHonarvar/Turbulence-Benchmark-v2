def all_left_truncatable_prime(numbers):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable(num):
        if '0' in str(num):
            return False
        s = str(num)
        for i in range(len(s)):
            if not is_prime(int(s[i:])):
                return False
        return True
    x = numbers[24]
    result = []
    for num in range(2, x):
        if is_prime(num) and is_left_truncatable(num):
            result.append(num)
    return result