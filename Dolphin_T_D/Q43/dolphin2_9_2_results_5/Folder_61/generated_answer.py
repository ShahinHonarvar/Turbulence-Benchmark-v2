def find_primes_between_indices(lst):
    primes = []
    for number in lst[3:9]:
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                primes.append(number)
    primes.sort()
    return primes