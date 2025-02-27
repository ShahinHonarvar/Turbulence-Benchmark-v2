def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_right_truncatable_primes(num):
    primes = []
    for i in range(10 ** len(str(num)) - 1, 0, -1):
        temp_num = num + i
        if is_prime(temp_num) and all((is_prime(int(str(temp_num)[:j])) for j in range(len(str(temp_num)), 0, -1))):
            primes.append(temp_num)
    return primes

def all_right_truncatable_prime(tup):
    x = tup[370]
    primes = get_right_truncatable_primes(x - 1)
    return sorted(primes, reverse=True)