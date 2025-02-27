def find_primes_between_indices(list_of_integers):
    primes = []
    for num in list_of_integers[24:33]:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return sorted(primes, reverse=True)