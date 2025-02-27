from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[177]
    result = []
    for num in range(2, x):
        truncated_num = num
        is_truncatable = True
        while truncated_num > 0:
            if not isprime(truncated_num):
                is_truncatable = False
                break
            truncated_num //= 10
        if is_truncatable:
            result.append(num)
    return sorted(result)