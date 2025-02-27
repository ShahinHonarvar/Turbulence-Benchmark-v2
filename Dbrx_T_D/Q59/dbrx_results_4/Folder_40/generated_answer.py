def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def remove_leading_digit(n):
    return int(str(n)[1:])

def all_left_truncatable_prime(t):
    primes = []
    x = t[10]
    for num in range(1, x):
        if is_prime(num):
            is_left_truncatable_prime = True
            tmp_num = num
            while tmp_num > 0:
                if not is_prime(tmp_num):
                    is_left_truncatable_prime = False
                    break
                tmp_num = remove_leading_digit(tmp_num)
        if is_left_truncatable_prime:
            primes.append(num)
    return sorted(primes, reverse=True)