def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

def prime_factors(integer_list):
    return {i for i in range(2, integer_list[51] + 1) if integer_list[51] % i == 0 and is_prime(i)}