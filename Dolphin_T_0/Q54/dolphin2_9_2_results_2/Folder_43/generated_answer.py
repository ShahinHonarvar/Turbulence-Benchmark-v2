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

def right_truncatable_prime(p):
    return all((is_prime(int(str(p)[i:])) for i in range(1, len(str(p)))))

def all_right_truncatable_prime(x):
    prime = [i for i in range(2, x) if is_prime(i)]
    return sorted([i for i in prime if right_truncatable_prime(i)], reverse=True)