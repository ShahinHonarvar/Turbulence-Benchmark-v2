from sympy import isprime

def all_left_truncatable_prime(x):
    result = []
    for num in range(3, x):
        str_num = str(num)
        if not '0' in str_num and all((isprime(int(str_num[i:])) for i in range(1, len(str_num)))):
            result.append(num)
    return sorted(result)