def factorize(n):
    factors = []
    for divisor in range(2, int(n ** 0.5) + 1):
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
    if n > 1:
        factors.append(n)
    return factors

def all_left_right_truncatable_prime(x):
    truncatable_primes = []
    for num in range(2, x + 1):
        if all((digit != '0' for digit in str(num))) and is_prime(num):
            str_num = str(num)
            for i in range(1, len(str_num)):
                left_num = int(str_num[:i])
                right_num = int(str_num[i:])
                if not (is_prime(left_num) and is_prime(right_num)):
                    break
            else:
                truncatable_primes.append(num)
    return sorted(truncatable_primes)

def is_prime(num):
    if num <= 1:
        return False
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            return False
    return True