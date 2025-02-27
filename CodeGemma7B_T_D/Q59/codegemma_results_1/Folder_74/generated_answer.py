import math

def all_left_truncatable_prime(x):
    a = [i for i in range(2, x) if all((j % i != 0 for j in range(2, int(math.sqrt(i)) + 1)))]
    return [i for i in a if all((str(i)[j:] in a for j in range(len(str(i)) - 1)))]