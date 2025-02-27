def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(t):
    x = t[41]
    primes = []
    for num in reversed(range(2, x)):
        if is_prime(num):
            str_num = str(num)
            for i in range(len(str_num) - 1):
                if str_num[i] == '0':
                    break
                if not is_prime(int(str_num[i:])):
                    break
            else:
                primes.append(num)
    return primes