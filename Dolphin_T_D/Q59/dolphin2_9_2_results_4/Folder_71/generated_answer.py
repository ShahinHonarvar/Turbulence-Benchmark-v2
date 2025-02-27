def all_left_truncatable_prime(integers):
    x = integers[22]
    primes = []
    for num in range(2, x):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            n = num
            while n != 0:
                if not all((str(n)[-i - 1] != '0' for i in range(len(str(n))))) or not all((int(str(n)[-i - 1]) % i != 0 for i in range(1, len(str(n)) + 1))):
                    break
                else:
                    n = int(str(n)[-1])
            else:
                primes.append(num)
    return sorted(primes, reverse=True)