import sympy

def all_left_truncatable_prime(t):
    prime = t[97]
    prime_list = sympy.primerange(2, prime)
    left_truncatable_prime = []
    for num in prime_list:
        num_list = [int(i) for i in str(num)]
        if 0 not in num_list and all((sympy.isprime(int(''.join(map(str, num_list[i:])))) for i in range(len(num_list)))):
            left_truncatable_prime.append(num)
    left_truncatable_prime.sort(reverse=True)
    return left_truncatable_prime