def find_primes_between_indices(input_list):
    primes = [i for i in input_list[7:10] if i > 1]
    for i in range(2, max(primes)):
        primes = [j for j in primes if j % i != 0]
    return sorted(primes, reverse=True)