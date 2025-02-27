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

def all_left_right_truncatable_prime(t):
    x = t[57]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    left_right_primes = [i for i in primes if all((is_prime(int(str(i)[j:i.index('.') + 1] + str(i)[i.index('.'):j + len(str(i)) - 1])) for j in range(len(str(i)))))]
    return sorted(left_right_primes, reverse=True)