from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[55]
    result = []
    if x > 2:
        for num in range(2, x):
            str_num = str(num)
            truncatable = True
            while str_num:
                if not isprime(int(str_num)):
                    truncatable = False
                    break
                str_num = str_num[:-1]
            if truncatable:
                result.append(num)
    return sorted(result)