from sympy import isprime

def all_right_truncatable_prime(x):
    prime = []
    for i in range(2, x):
        if isprime(i):
            num = str(i)
            for j in range(len(num)):
                if isprime(int(num[:len(num) - j])):
                    prime.append(int(num[:len(num) - j]))
    return sorted(list(set(prime)))