def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    if len(lst) < 94:
        return []
    selected_elements = lst[89:94]
    primes = [x for x in selected_elements if is_prime(x)]
    return sorted(primes, reverse=True)