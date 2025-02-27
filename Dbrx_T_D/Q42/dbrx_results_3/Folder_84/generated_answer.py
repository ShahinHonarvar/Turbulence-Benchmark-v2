def prime_factors(int_list):
    primes = set()
    num = int_list[685]
    for i in range(2, num + 1):
        if num % i == 0:
            is_prime = True
            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.add(i)
                while num % i == 0:
                    num //= i
    return primes