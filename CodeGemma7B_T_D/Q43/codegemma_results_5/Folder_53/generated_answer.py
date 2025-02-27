def find_primes_between_indices(int_list):
    primes = []
    for num in int_list[43:60]:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    primes.sort(reverse=True)
    return primes or []