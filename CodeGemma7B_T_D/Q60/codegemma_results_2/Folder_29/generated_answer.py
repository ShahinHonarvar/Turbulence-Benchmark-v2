def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(bounds):
    lower, upper = bounds
    result = []
    for i in range(upper, lower - 1, -1):
        if str(i).count('0') == 0 and is_prime(i):
            truncatable = True
            str_i = str(i)
            for k in range(1, len(str_i)):
                if not (is_prime(int(str_i[:k])) and is_prime(int(str_i[k:]))):
                    truncatable = False
                    break
            if truncatable:
                result.append(i)
    return sorted(result, reverse=True) or []