def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[100]
    result = []
    for i in range(2, x + 1):
        if str(i).count('0') == 0 and is_prime(i):
            str_i = str(i)
            for j in range(1, len(str_i)):
                if not (is_prime(int(str_i[:j])) and is_prime(int(str_i[j:]))):
                    break
            else:
                result.append(i)
    return sorted(result)