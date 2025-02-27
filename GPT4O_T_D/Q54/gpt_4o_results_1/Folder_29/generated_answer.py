from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[55]
    right_trunc_primes = []
    for num in range(2, x):
        str_num = str(num)
        is_right_trunc_prime = True
        while str_num:
            if not isprime(int(str_num)):
                is_right_trunc_prime = False
                break
            str_num = str_num[:-1]
        if is_right_trunc_prime:
            right_trunc_primes.append(num)
    return sorted(right_trunc_primes, reverse=True)