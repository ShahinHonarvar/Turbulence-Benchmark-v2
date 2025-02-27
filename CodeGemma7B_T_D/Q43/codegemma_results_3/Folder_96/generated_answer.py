def find_primes_between_indices(int_list):
    primes = []
    for number in int_list[31:68]:
        if number % 2 != 0 and number % 3 != 0:
            prime = True
            for i in range(5, int(number ** 0.5) + 1, 6):
                if number % i == 0 or number % (i + 2) == 0:
                    prime = False
                    break
            if prime:
                primes.append(number)
    primes.sort(reverse=True)
    return primes if primes else []