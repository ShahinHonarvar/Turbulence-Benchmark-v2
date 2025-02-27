def all_left_truncatable_prime(n):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def trunc(num):
        return [int(num[i:]) for i in range(1, len(num))]

    def left_truncatable(n):
        num = str(n)
        return all((is_prime(x) for x in trunc(num)))
    x = n[77]
    result = [i for i in range(x - 1, 1, -1) if is_prime(i) and left_truncatable(i)]
    return result