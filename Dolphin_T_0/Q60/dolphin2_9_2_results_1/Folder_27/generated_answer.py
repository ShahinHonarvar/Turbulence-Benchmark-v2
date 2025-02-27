def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[79]
    primes = [i for i in range(x, 1, -1) if is_prime(i)]
    truncables = [i for i in primes if len(str(i)) == 1 or (len(str(i)) > 2 and is_prime(int(str(i)[1:])) and is_prime(int(str(i)[:-1])))]
    return sorted(truncables, reverse=True)