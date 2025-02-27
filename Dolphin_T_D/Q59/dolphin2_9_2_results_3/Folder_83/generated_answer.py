def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(lst):
    x = lst[24]
    primes_list = []
    for num in range(2, x):
        if all((is_prime(int(str(num)[i:])) for i in range(len(str(num)) - 1, -1, -1))):
            primes_list.append(num)
    return sorted(primes_list)