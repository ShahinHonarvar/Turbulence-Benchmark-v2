def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x_tuple):
    x = x_tuple[74]
    result = []
    for num in range(1, x + 1):
        if is_prime(num):
            digits = len(str(num))
            for i in range(digits - 1):
                if not is_prime(int(str(num)[i + 1:])):
                    break
                if not is_prime(int(str(num)[:-i - 1])):
                    break
            else:
                result.append(num)
    return sorted(result)