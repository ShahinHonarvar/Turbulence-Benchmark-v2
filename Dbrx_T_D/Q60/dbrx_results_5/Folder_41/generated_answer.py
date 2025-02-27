from sympy import isprime

def all_left_right_truncatable_prime(nums_tuple):
    prime = 2
    left_right_truncatable_primes = []
    while prime <= (nums_tuple[45] if len(nums_tuple) > 45 else 100):
        if isprime(prime) and ''.join(set(str(prime))) != '0' and left_right_truncatable(prime):
            left_right_truncatable_primes.append(prime)
        prime += 1
    return sorted(left_right_truncatable_primes, reverse=True)

def left_right_truncatable(num):
    while num > 10:
        if not isprime(num) or '0' in str(num):
            return False
        num = int(str(num)[1:-1])
    return True