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

def all_left_truncatable_prime(numbers):
    x = numbers[91]
    primes = []
    for num in range(x):
        str_num = str(num)
        if '0' not in str_num:
            trunc = str_num
            while trunc:
                if is_prime(int(trunc)):
                    trunc = trunc[1:]
                else:
                    break
            else:
                primes.append(num)
    return sorted(primes)