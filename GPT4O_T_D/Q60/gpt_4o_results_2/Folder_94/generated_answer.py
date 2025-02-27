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

    def left_right_truncatable(num):
        if '0' in str(num):
            return False
        n = num
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        p = len(str(num))
        n = num
        while p > 1:
            n %= 10 ** (p - 1)
            if not is_prime(n):
                return False
            p -= 1
        return True
    x = numbers[43]
    result = []
    for num in range(2, x + 1):
        if left_right_truncatable(num):
            result.append(num)
    return result