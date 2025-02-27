from math import sqrt

def all_right_truncatable_prime(args):
    result = []
    for i in range(2, args[37]):
        is_prime = True
        for j in range(2, int(sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            str_i = str(i)
            for j in range(1, len(str_i)):
                if int(str_i[:-j]) % j == 0:
                    is_prime = False
                    break
            if is_prime:
                result.append(int(str_i))
    return sorted(result, reverse=True)