def find_primes_between_indices(list_of_integers):
    primes = []
    for number in list_of_integers[14:69]:
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                primes.append(number)
    primes.sort(reverse=True)
    return primes