def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[29]
    primes = []
    for num in reversed(range(2, x + 1)):
        if is_prime(num):
            str_num = str(num)
            while str_num and is_prime(int(str_num)):
                primes.append(int(str_num))
                str_num = str_num[1:-1]
    return primes