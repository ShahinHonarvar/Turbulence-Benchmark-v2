from sympy import isprime

def all_right_truncatable_prime(x):
    sequence = []
    for i in range(1, 10):
        num = 0
        for j in str(i):
            num = num * 10 + int(j)
            if isprime(num) and num < x:
                sequence.append(num)
    return sorted(sequence)