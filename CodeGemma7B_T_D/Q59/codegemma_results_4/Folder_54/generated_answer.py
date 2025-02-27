def all_left_truncatable_prime(max_prime):
    return sorted([i for i in range(max_prime) if is_left_truncatable_prime(i)], reverse=True)

def is_left_truncatable_prime(prime):
    if len(str(prime)) == len(str(prime)) * '1':
        return False
    if prime % 2 == 0 or prime % 5 == 0:
        return False
    for i in range(2, int(prime ** 0.5) + 1):
        if prime % i == 0:
            return False
    return all((is_prime(int(str(prime)[j:])) for j in range(1, len(str(prime)))))

def is_prime(prime):
    if prime % 2 == 0 or prime % 5 == 0:
        return False
    for i in range(5, int(prime ** 0.5) + 1, 6):
        if prime % i == 0 or prime % (i + 2) == 0:
            return False
    return True