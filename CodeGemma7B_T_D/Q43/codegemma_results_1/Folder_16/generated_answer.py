def find_primes_between_indices(list):
    primes = sorted([num for num in list[424:553] if all((num % i != 0 for i in range(2, num)))], reverse=True)
    return primes if primes else []