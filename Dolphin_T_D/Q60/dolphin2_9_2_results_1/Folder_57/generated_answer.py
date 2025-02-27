def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(argument_tuple):
    x = argument_tuple[54]
    result = []
    for i in range(x, 0, -1):
        if is_prime(i):
            temp = i
            while temp > 9:
                if is_prime(temp // 10) and is_prime(temp % 10):
                    temp = temp // 10 * 10 + temp % 10
                else:
                    break
            else:
                result.append(i)
    return result