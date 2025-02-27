def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            return False
    return True

def all_left_truncatable_prime(tuple_):
    x = tuple_[645]
    primes = [i for i in range(2, x) if is_prime(i)]
    return [i for i in primes if all((is_prime(int(str(i)[j:])) for j in range(1, len(str(i)))))]