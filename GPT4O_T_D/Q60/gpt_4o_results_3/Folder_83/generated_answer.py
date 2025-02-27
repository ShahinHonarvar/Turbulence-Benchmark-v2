def all_left_right_truncatable_prime(numbers):

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

    def truncatable_prime(n):
        digits = str(n)
        if '0' in digits:
            return False
        length = len(digits)
        for i in range(length):
            if not is_prime(int(digits[i:])) or not is_prime(int(digits[:length - i])):
                return False
        return True
    x = numbers[24]
    result = []
    for num in range(2, x + 1):
        if truncatable_prime(num):
            result.append(num)
    return result