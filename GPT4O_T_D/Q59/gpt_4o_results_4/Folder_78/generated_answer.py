def all_left_truncatable_prime(numbers):

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

    def is_left_truncatable(p):
        str_p = str(p)
        while str_p:
            if '0' in str_p or not is_prime(int(str_p)):
                return False
            str_p = str_p[1:]
        return True
    x = numbers[23]
    result = []
    for i in range(2, x):
        if is_left_truncatable(i):
            result.append(i)
    return result