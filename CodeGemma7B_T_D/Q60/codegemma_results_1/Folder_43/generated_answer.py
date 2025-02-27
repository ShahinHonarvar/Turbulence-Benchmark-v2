from sympy import isprime

def all_left_right_truncatable_prime(x):
    prime = [n for n in range(2, x + 1) if isprime(n)]
    result = []
    for number in prime:
        if '0' in str(number):
            continue
        left_prime = [int(str(number)[:i]) for i in range(2, len(str(number)) + 1)]
        right_prime = [int(str(number)[i:]) for i in range(1, len(str(number)) + 1)]
        for prime in left_prime + right_prime:
            if not isprime(prime):
                break
        else:
            if number not in result:
                result.append(number)
    return result