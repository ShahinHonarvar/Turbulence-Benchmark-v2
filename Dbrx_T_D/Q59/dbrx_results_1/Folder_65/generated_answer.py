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

def left_truncatable_primes(limit):
    result = []
    for num in range(1, limit):
        if is_prime(num):
            str_num = str(num)
            if int(str_num[0]) != 0 and all((int(str_num[i:]) > 0 and is_prime(int(str_num[i:])) for i in range(1, len(str_num)))):
                result.append(num)
    return sorted(result)