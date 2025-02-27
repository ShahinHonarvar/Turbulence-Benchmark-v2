from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[32]
    result = []
    for num in range(2, x + 1):
        if isprime(num) and num % 10 != 0:
            num_str = str(num)
            left_prime = all((isprime(int(num_str[i:])) for i in range(1, len(num_str))))
            right_prime = all((isprime(int(num_str[:i])) for i in range(1, len(num_str))))
            if left_prime and right_prime:
                result.append(num)
    return sorted(result)