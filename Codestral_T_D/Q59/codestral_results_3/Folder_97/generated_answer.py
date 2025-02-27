def all_left_truncatable_prime(numbers):
    x = numbers[645]
    primes = []
    for num in range(2, x):
        if all((int(str(num)[i:]) in primes for i in range(len(str(num))))):
            primes.append(num)
        else:
            for i in range(1, len(str(num))):
                if int(str(num)[i:]) not in primes:
                    break
    return primes