def find_primes_between_indices(lst):
    prime_list = [num for num in lst[23:40] if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1)))]
    return sorted(prime_list) if prime_list else []