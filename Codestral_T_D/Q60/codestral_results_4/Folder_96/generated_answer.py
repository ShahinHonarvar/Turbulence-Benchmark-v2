from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[29]
    result = []
    for num in range(11, x + 1):
        if '0' not in str(num):
            if isprime(num):
                truncatable = True
                temp = num
                while temp > 0:
                    temp //= 10
                    if temp < 10 or not isprime(temp):
                        truncatable = False
                        break
                temp = num
                while temp > 0:
                    temp = int(str(temp)[1:])
                    if temp < 10 or not isprime(temp):
                        truncatable = False
                        break
                if truncatable:
                    result.append(num)
    return sorted(result)