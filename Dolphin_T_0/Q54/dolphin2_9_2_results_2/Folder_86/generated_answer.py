def all_right_truncatable_prime(t):
    x = t[126]
    primes = [2, 3, 5, 7]
    for num in range(11, x):
        if all((num % i != 0 for i in primes)):
            primes.append(num)
            truncatable = True
            for digit in str(num):
                if int(digit) not in primes:
                    truncatable = False
                    break
            if truncatable:
                for i in range(len(str(num)) - 1):
                    if int(str(num)[i:]) not in primes:
                        truncatable = False
                        break
            if truncatable:
                return sorted(primes, reverse=True)
    return []