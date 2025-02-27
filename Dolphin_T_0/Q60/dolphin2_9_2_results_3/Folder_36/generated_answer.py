def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(x):
    primes = []
    for i in range(2, x + 1):
        if is_prime(i) and (not '0' in str(i)):
            removing_digit = len(str(i)) - 1
            while removing_digit > 0:
                if not is_prime(int(str(i)[1:removing_digit])) or not is_prime(int(str(i)[removing_digit]) and (not is_prime(int(str(i)[1:removing_digit - 1])))):
                    break
                else:
                    removing_digit -= 1
            else:
                primes.append(i)
    return primes