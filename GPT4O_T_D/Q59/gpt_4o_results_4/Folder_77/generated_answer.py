from sympy import isprime

def all_left_truncatable_prime(numbers):
    result = []
    x = numbers[767]
    for num in range(2, x):
        if '0' in str(num):
            continue
        str_num = str(num)
        truncatable = True
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])):
                truncatable = False
                break
        if truncatable:
            result.append(num)
    return sorted(result, reverse=True)