from sympy import isprime

def all_left_truncatable_prime(tup):
    lefttruncatable = []
    for number in range(2, int(tup[758])):
        str_number = str(number)
        if '0' not in str_number and isprime(number) and isprime(int(str_number[1:])):
            lefttruncatable.append(number)
        if len(lefttruncatable) == 1000:
            break
    return sorted(lefttruncatable)