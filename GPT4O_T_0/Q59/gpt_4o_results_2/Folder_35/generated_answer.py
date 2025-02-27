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

    def is_left_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        while str_n:
            if not is_prime(int(str_n)):
                return False
            str_n = str_n[1:]
        return True
    x = numbers[177]
    result = []
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            result.append(num)
    return result