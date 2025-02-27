def all_right_truncatable_prime(input_tuple):

    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_right_truncatable(n):
        while n > 10:
            if not is_prime(n):
                return False
            n //= 10
        return is_prime(n)
    x = input_tuple[42]
    result = []
    for i in range(x - 1, 0, -1):
        if is_right_truncatable(i):
            result.append(i)
    result.sort()
    return result