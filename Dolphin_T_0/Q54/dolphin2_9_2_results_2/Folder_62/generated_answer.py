def all_right_truncatable_prime(t):
    x = t[70]
    primes = []
    for number in range(2, x):
        if all((number % i != 0 for i in range(2, number))):
            trunc = number
            while trunc > 0:
                if trunc < number:
                    primes.append(number)
                    break
                trunc = int(str(trunc)[:-1])
    return sorted(list(set(primes)))