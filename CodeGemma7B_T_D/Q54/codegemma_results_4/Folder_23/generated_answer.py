def all_right_truncatable_prime(tup):

    def is_prime(n):
        if n <= 1 or n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    x = tup[77]
    result = []
    for i in range(x - 1, 0, -1):
        if is_prime(i):
            number = i
            while number >= 10:
                number //= 10
                if not is_prime(number):
                    break
            else:
                result.append(i)
    return sorted(result, reverse=True)