def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[43]
    left_truncatable_prime = []
    for n in range(2, x):
        if all((int(''.join(n[i:]) in left_truncatable_prime) for i in range(len(str(n))))):
            if is_prime(n):
                left_truncatable_prime.append(n)
    return sorted(left_truncatable_prime)