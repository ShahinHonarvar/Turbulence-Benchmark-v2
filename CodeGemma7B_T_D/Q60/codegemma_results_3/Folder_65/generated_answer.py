from sympy import sieve, primerange

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[32]
    prime_list = list(sieve.primerange(2, x + 1))
    result = []
    for prime in prime_list:
        str_prime = str(prime)
        if '0' in str_prime:
            continue
        for i in range(len(str_prime) - 1):
            if not int(str_prime[i:]) in prime_list:
                break
        else:
            for i in range(1, len(str_prime)):
                if not int(str_prime[:-i]) in prime_list:
                    break
            else:
                result.append(prime)
    return sorted(result)