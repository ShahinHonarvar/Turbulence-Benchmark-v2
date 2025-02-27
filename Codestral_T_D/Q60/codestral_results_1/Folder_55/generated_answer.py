def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = n // 10
        return True

    def is_right_truncatable(n):
        str_n = str(n)
        while len(str_n) > 0:
            if not is_prime(int(str_n)):
                return False
            str_n = str_n[:-1]
        return True
    x = numbers[73]
    lst = []
    for num in range(2, x + 1):
        if is_prime(num) and is_left_truncatable(num) and is_right_truncatable(num):
            lst.append(num)
    lst.sort(reverse=True)
    return lst