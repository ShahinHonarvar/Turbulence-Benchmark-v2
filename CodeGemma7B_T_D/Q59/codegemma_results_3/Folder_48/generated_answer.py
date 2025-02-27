from sympy import isprime

def all_left_truncatable_prime(n):
    result = []
    for i in range(1, n):
        str_i = str(i)
        if '0' not in str_i:
            is_prime = True
            for j in range(len(str_i)):
                num = int(str_i[j:])
                if not isprime(num):
                    is_prime = False
                    break
            if is_prime:
                result.append(i)
    return sorted(result)