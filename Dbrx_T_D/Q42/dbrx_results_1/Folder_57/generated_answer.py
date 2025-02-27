def prime_factors(number_list):
    primes = set()
    for num in number_list:
        if num > 1:
            for i in range(2, num + 1):
                if num % i == 0:
                    if is_prime(i):
                        primes.add(i)
    return primes

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True