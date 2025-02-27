def find_primes_between_indices(int_list):
    primes = []
    for num in int_list[57:65]:
        if all((num % i != 0 for i in range(2, num))):
            primes.append(num)
    primes.sort(reverse=True)
    return primes if primes else []