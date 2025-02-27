def find_primes_between_indices(num_list):
    primes = []
    for num in num_list[19:72]:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return sorted(primes) if primes else []