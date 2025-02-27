from sympy import isprime

def all_right_truncatable_prime(x):
    left = x[49]
    count = 0
    result = []
    for number in range(left):
        if isprime(number):
            new_number = number
            condition = True
            while new_number != 0:
                digit = new_number % 10
                new_number //= 10
                if not isprime(digit):
                    condition = False
                    break
                if count != left - 1:
                    new_number -= digit * 10 ** (count + 1)
                    count += 1
                else:
                    result.append(number)
                    break
    return sorted(result)