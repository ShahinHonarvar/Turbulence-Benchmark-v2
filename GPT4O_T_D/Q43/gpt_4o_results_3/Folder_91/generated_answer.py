def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes_between_indices(lst):
    if len(lst) < 2:
        return []
    start, end = (lst[0], lst[1])
    primes = [x for x in lst[start:end + 1] if is_prime(x)]
    return sorted(primes)