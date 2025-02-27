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

def find_primes_between_indices(lst):
    primes = []
    for number in lst[31:68]:
        if is_prime(number):
            primes.append(number)
    primes.sort(reverse=True)
    return primes