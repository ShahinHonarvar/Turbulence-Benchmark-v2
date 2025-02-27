def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[1]
    right_truncatable_primes = []
    for num in range(11, x):
        str_num = str(num)
        while len(str_num) > 1:
            if not is_prime(int(str_num)):
                break
            str_num = str_num[:-1]
        else:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)