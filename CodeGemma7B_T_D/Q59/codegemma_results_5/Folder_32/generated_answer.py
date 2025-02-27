from sympy import isprime

def all_left_truncatable_prime(x):
    result = []
    for i in range(1, x):
        num = str(i)
        if all((digit != '0' for digit in num)) and all((isprime(int(num[index:])) for index in range(1, len(num)))):
            result.append(int(num))
    return sorted(result)