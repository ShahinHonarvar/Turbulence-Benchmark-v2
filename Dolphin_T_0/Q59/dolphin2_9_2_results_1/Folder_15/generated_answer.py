def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[6]
    res = []
    for i in range(x - 1, 0, -1):
        if is_prime(i) and all(is_prime(int(str(i)[1:]))):
            res.append(i)
    return res