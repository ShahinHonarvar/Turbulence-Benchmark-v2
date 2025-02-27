def all_left_right_truncatable_prime(numbers):

    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_truncatable(num):
        s = str(num)
        if '0' in s:
            return False
        length = len(s)
        for i in range(1, length):
            left_trunc = int(s[i:])
            right_trunc = int(s[:-i])
            if not (is_prime(left_trunc) and is_prime(right_trunc)):
                return False
        return True
    x = numbers[61]
    result = []
    for num in range(11, x + 1):
        if is_prime(num) and is_truncatable(num):
            result.append(num)
    return result