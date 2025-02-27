def all_right_truncatable_prime(num_tuple):
    x = num_tuple[52]
    result = []
    for i in range(x - 1, 2, -1):
        if is_prime(i):
            tmp = int(str(i)[:-1])
            while tmp > 1:
                if not is_prime(tmp):
                    break
                tmp = int(str(tmp)[:-1])
            else:
                result.append(i)
    return sorted(result, reverse=True)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True