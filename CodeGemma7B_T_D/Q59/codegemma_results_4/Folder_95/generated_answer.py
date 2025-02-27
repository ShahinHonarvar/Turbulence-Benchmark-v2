def all_left_truncatable_prime(tuple):
    return sorted([i for i in tuple if all((j in '123456789' for j in str(i))) and all_prime_less_than(i) and all_prime_less_than(int(str(i)[1:]))])

def all_prime_less_than(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True