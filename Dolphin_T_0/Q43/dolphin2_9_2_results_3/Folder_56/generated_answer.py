def find_primes_between_indices(lst):
    primeNumbers = [x for x in lst[40:69] if all((x % i != 0 for i in range(2, int(x ** 0.5) + 1)))]
    primeNumbers.sort(reverse=True)
    return primeNumbers