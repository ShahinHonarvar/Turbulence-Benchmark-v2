import itertools

def all_right_truncatable_prime(tupl):
    x = tupl[32]
    right_truncatable_prime = []
    for i in range(2, x):
        if all_prime(i) and all_right_truncatable(i):
            right_truncatable_prime.append(i)
    return sorted(right_truncatable_prime)

def all_prime(i):
    if i <= 1:
        return False
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            return False
    return True

def all_right_truncatable(i):
    for j in range(1, len(str(i))):
        k = int(str(i)[:-j])
        if all_prime(k) == False:
            return False
    return True