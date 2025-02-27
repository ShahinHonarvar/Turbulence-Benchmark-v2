def all_right_truncatable_prime(args):
    x = args[4]
    result = []
    for i in range(2, x):
        if is_prime(i):
            str_i = str(i)
            for j in range(1, len(str_i)):
                if not is_prime(int(str_i[:-j])):
                    break
            else:
                result.append
    return result

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True