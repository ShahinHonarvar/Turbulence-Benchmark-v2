def all_left_truncatable_prime(numbers):
    x = numbers[98]
    primes = []
    for num in range(2, x):
        if all((int(str(num)[i:]) in primes for i in range(len(str(num))))):
            primes.append(num)
        else:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return sorted(primes)