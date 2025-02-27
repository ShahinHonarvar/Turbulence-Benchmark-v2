def find_primes_between_indices(int_list):
    primes = [num for num in int_list[6:8] if all((num % i for i in range(2, int(num ** 0.5) + 1)))]
    primes.sort(reverse=True)
    return primes or []