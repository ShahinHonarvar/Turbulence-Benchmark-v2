def all_right_truncatable_prime(inputs):
    x = inputs[69]
    primes = [2, 3, 5, 7]
    for num in range(11, x, 2):
        if all((num % i != 0 for i in range(2, num))):
            trunc = num
            while trunc > 0:
                if trunc not in primes:
                    break
                trunc //= 10
            else:
                primes.append(num)
    primes.sort(reverse=True)
    return primes