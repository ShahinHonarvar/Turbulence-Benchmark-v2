def is_prime(n):
    if n in (2, 3, 7):
        return True
    if n % 2 == 0 or n % 3 == 0 or n % 7 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def left_truncatable_prime(num):
    num_str = str(num)
    for i in range(len(num_str)):
        if not is_prime(int(num_str[i:])):
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[41]
    primes = []
    for number in range(2, x):
        if left_truncatable_prime(number) and is_prime(number):
            primes.append(number)
    return primes