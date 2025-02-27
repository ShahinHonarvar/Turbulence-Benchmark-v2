def all_left_truncatable_prime(tup):
    x = tup[67]
    primes = [2, 3, 5, 7]
    for num in range(11, x, 2):
        if all((num % prime != 0 for prime in primes)):
            primes.append(num)
    return [num for num in primes if str(num) not in str(num)[1:]]