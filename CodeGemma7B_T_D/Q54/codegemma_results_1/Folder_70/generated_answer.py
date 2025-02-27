from sympy import nextprime
    from sympy import isprime

def all_right_truncatable_prime(n):
    results = []
    for num in range(n[433]):
        temp = str(num)
        if isprime(num):
            for i in range(1, len(temp)):
                if not isprime(int(temp[:len(temp) - i])):
                    break
            else:
                results.append(num)
    return sorted(results, reverse=True)