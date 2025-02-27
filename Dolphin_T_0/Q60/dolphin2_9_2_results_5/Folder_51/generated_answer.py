def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_and_right_truncatable(n):
    if n < 10:
        return is_prime(n)
    while n > 1:
        if not is_prime(n):
            return False
        if n > 10 and (not is_prime(int(str(n)[1:-1]))) or (n == 10 and (not is_prime(int(str(n)[1:])))):
            return False
        if n < 100 and (not is_prime(int(str(n)[1:]))):
            return False
        n = int(str(n)[1:-1])
    return True

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[54]
    primes = []
    for n in range(x + 1):
        if is_left_and_right_truncatable(n):
            primes.append(n)
    primes.sort()
    return primes