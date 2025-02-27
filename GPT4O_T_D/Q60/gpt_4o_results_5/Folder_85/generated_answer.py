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

    def is_left_right_truncatable_prime(p):
        str_p = str(p)
        if '0' in str_p:
            return False
        length = len(str_p)
        for i in range(length):
            if not is_prime(int(str_p[i:])) or not is_prime(int(str_p[:length - i])):
                return False
        return True
    x = numbers[94]
    result = []
    for i in range(2, x + 1):
        if is_left_right_truncatable_prime(i):
            result.append(i)
    return result