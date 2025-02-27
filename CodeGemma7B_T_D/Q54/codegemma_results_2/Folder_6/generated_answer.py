def all_right_truncatable_prime(tup):
    x = tup[74]
    result = []
    for i in range(2, x):
        if is_prime(i):
            str_i = str(i)
            for j in range(1, len(str_i)):
                if not is_prime(int(str_i[:-j])):
                    break
            else:
                result.append(i)
    return sorted(result)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True