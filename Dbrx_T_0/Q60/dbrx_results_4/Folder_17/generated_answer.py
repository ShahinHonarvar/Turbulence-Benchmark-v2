from sympy import isprime

def all_left_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[36]
    ltr_primes = []
    for num in range(2, x + 1):
        if isprime(num) and '0' not in str(num):
            is_ltr_prime = True
            for i in range(1, len(str(num))):
                if not isprime(int(str(num)[i:])) or not isprime(int(str(num)[:-i])):
                    is_ltr_prime = False
                    break
            if is_ltr_prime:
                ltr_primes.append(num)
    return sorted(ltr_primes, reverse=True)