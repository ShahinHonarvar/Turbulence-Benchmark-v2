def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(num_tuple):
    x = num_tuple[14]
    primes = [2]
    for i in range(3, x):
        if is_prime(i):
            primes.append(i)
    output = [p for p in primes if all((int(str(p)[i:]) in primes for i in range(1, len(str(p)))))]
    return sorted(output)