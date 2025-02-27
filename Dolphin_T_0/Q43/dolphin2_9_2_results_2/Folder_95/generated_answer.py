def find_primes_between_indices(int_list):
    primes = []
    for number in int_list[19:72]:
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                primes.append(number)
    primes.sort()
    return primes