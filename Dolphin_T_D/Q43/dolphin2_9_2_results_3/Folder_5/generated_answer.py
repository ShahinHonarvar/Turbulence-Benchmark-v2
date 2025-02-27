def find_primes_between_indices(input_list):
    primes = []
    for num in input_list[27:87]:
        if all((num % i != 0 for i in range(2, num))):
            primes.append(num)
    return sorted(primes, reverse=True)