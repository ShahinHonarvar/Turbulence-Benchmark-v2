from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[50]
    result = []
    for num in range(2, x + 1):
        if isprime(num) and (not '0' in str(num)):
            is_ltr_prime = True
            for i in range(1, len(str(num))):
                if not isprime(int(str(num)[i:])) or not isprime(int(str(num)[:-i])):
                    is_ltr_prime = False
                    break
            if is_ltr_prime:
                result.append(num)
    return sorted(result, reverse=True) if result else []