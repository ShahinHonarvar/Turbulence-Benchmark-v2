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
        str_n = str(n)
        while len(str_n) > 1:
            str_n = str_n[1:-1]
            if not str_n or not is_prime(int(str_n)):
                return False
        return is_prime(n)
    x = numbers[792]
    result = []
    for num in range(11, x + 1):
        if '0' not in str(num) and is_prime(num) and truncatable_prime(num):
            result.append(num)
    return result