from math import sqrt

def all_right_truncatable_prime(tup):
    x = tup[429]
    result = []
    for i in range(2, x):
        if is_prime(i):
            for j in range(1, int(sqrt(i)) + 1):
                if i % j == 0:
                    break
            else:
                temp = format(i, 'd')
                for k in range(1, len(temp)):
                    if not is_prime(int(temp[0:k])):
                        break
                else:
                    result.append(i)
    result.sort(reverse=True)
    return result

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True