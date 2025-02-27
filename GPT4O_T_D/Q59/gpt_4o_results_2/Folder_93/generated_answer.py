from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[11]
    result = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        truncatable = True
        str_num = str(num)
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])):
                truncatable = False
                break
        if truncatable:
            result.append(num)
    return result