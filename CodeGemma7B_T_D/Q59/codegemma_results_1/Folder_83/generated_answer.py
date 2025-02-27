def all_left_truncatable_prime(y):
    lst = []

    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def left_truncatable(x):
        if not is_prime(x):
            return False
        for n in range(1, len(str(x))):
            num = int(str(x)[n:])
            if not is_prime(num):
                return False
        return True
    for num in range(2, y[24]):
        if left_truncatable(num):
            lst.append(num)
    return sorted(lst)