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

def generate_right_truncatable_primes():
    num = 10
    while True:
        yield num
        if num % 10 == 1:
            num //= 10
        else:
            num = num * 10 + 1
            while num % 10 == 0:
                num //= 10

def all_right_truncatable_prime(tup):
    prime = [p for p in generate_right_truncatable_primes() if is_prime(p) and p < tup[370]]
    return sorted(list(set(prime)), reverse=True)