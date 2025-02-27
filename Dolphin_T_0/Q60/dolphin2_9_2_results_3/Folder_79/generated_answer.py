def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            return False
    return True

def trunc(n):
    return is_prime(int(n)) and all((is_prime(int(n[1:i])) and is_prime(int(n[i:len(n) - 1])) for i in range(1, len(n)))) and (n[-1] != '0') and (n[0] != '0')

def all_left_right_truncatable_prime(int_tuple):
    x = int_tuple[91]
    primes_list = []
    for i in range(2, x + 1):
        if trunc(str(i)):
            primes_list.append(i)
    return primes_list