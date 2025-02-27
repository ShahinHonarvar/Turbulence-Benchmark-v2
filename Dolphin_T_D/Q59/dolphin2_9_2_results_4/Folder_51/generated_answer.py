from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[54]
    prime_list = []
    for num in range(2, x):
        if isprime(num):
            left_trunc = [num]
            for digit in str(num):
                left_trunc.append(int(str(left_trunc[-1])) + 10 ** (len(str(left_trunc[-1])) - 1))
                if not isprime(left_trunc[-1]):
                    break
            else:
                prime_list.extend(left_trunc)
    return sorted(list(set(prime_list)))