from sympy import isprime

def all_left_right_truncatable_prime(upperbound):
    result = []
    for i in range(2, upperbound + 1):
        str_i = str(i)
        if '0' in str_i:
            continue
        is_prime = True
        for j in range(len(str_i)):
            if not isprime(int(str_i[j:])):
                is_prime = False
                break
        if is_prime:
            result.append(i)
    result.sort(reverse=True)
    return result