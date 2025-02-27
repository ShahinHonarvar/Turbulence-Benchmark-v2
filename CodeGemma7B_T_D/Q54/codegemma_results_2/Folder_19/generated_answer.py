from sympy import isprime, digits

def all_right_truncatable_prime(tup):
    x = tup[67]
    right_truncatable_primes = []
    for number in range(2, x):
        if isprime(number):
            for trailing in digits(str(number))[:-1]:
                prime = True
                for i in range(len(str(number)) - 1):
                    if not isprime(int(str(number)[:-i])):
                        prime = False
                        break
                if prime:
                    right_truncatable_primes.append(number)
    return sorted(right_truncatable_primes, reverse=True)