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

def find_primes_between_indices(int_list):
    if len(int_list) < 3:
        return []
    primes = [num for num in int_list[1:3] if is_prime(num)]
    return sorted(primes, reverse=True)