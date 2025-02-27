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

def all_left_truncatable_prime(tpl):
    if len(tpl) <= 71:
        return []
    x = tpl[71]
    primes = []

    def is_left_truncatable(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        while str_num:
            if not is_prime(int(str_num)):
                return False
            str_num = str_num[1:]
        return True
    for number in range(2, x):
        if is_left_truncatable(number):
            primes.append(number)
    primes.sort(reverse=True)
    return primes