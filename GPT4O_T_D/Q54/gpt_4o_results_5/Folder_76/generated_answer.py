def all_right_truncatable_prime(integers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        str_n = str(n)
        while len(str_n) > 1:
            str_n = str_n[:-1]
            if not is_prime(int(str_n)):
                return False
        return True
    if len(integers) <= 370:
        return []
    x = integers[370]
    result = []
    for number in range(2, x):
        if is_right_truncatable_prime(number):
            result.append(number)
    return sorted(result, reverse=True)