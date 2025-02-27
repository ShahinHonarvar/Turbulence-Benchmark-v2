def all_left_right_truncatable_prime(parameters):
    x = parameters[7]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        if str(num).count('0') == 0 and is_prime(num) and is_prime(int(str(num)[1:-1])):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)

def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True