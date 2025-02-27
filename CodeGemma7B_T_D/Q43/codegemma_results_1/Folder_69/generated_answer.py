def find_primes_between_indices(my_list):
    primes = [num for num in my_list[497:931] if all((num % i for i in range(2, num)))]
    return sorted(primes, reverse=True) if primes else []