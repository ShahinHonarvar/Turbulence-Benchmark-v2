def max_factor(x):
    for i in range(2, int(x ** 0.5) + 1):
        while x % i == 0:
            x = x / i
    if x > 1:
        return x
    return None

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[92]

    def is_left_truncatable_prime(x):
        temp = x
        while temp >= 10:
            temp = max_factor(temp)
            if not is_prime(temp):
                return False
        if is_prime(temp):
            return True
        return False

    def is_right_truncatable_prime(x):
        temp = x
        while temp >= 10:
            temp = temp % 10
            if not is_prime(temp):
                return False
        if is_prime(temp):
            return True
        return False
    result = []
    for i in range(2, x + 1):
        if is_left_truncatable_prime(i) and is_right_truncatable_prime(i):
            result.append(i)
    result.sort()
    return result