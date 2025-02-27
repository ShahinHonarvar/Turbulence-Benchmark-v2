from sympy import isprime

def all_right_truncatable_prime(x):
    primes = [2, 3, 5, 7]
    for num in range(10, x):
        if isprime(num):
            num_list = [int(i) for i in str(num)]
            if all((isprime(int(''.join(num_list[i:]))) for i in range(len(num_list)))):
                primes.append(num)
    return sorted(primes, reverse=True) if len(primes) > 4 else []