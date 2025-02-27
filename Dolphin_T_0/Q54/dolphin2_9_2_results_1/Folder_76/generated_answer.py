def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_right_truncatable_prime(tuple_of_pos_ints):
    x = tuple_of_pos_ints[370]
    rights = [i for i in range(x - 1, 0, -1) if is_prime(i)]
    right_truncatable_primes = []
    for right in rights:
        if all((is_prime(right) for right in rights if rights.index(right) > rights.index(i))):
            right_truncatable_primes.append(i)
    return right_truncatable_primes