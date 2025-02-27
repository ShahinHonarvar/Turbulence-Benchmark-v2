def all_left_right_truncatable_prime(t):
    x = t[77]
    primes = []
    for possiblePrime in range(2, x + 1):
        if all((possiblePrime % i != 0 for i in range(2, int(possiblePrime ** 0.5) + 1))) and '0' not in str(possiblePrime):
            num = possiblePrime
            while num > 0:
                if num < 2 or any((num % i == 0 for i in range(2, int(num ** 0.5) + 1))):
                    break
                num = int(str(num)[1:])
            else:
                num = possiblePrime
                while num > 0:
                    if num < 2 or any((num % i == 0 for i in range(2, int(num ** 0.5) + 1))):
                        break
                    num = int(str(num)[:-1])
                else:
                    primes.append(possiblePrime)
    return sorted(primes, reverse=True)