def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def right_truncatable_primes(num):
    primes = []
    while num > 0:
        if is_prime(num):
            primes.append(num)
        num //= 10
    return primes

def all_right_truncatable_prime(numbers):
    x = numbers[79]
    right_truncatable_primes_list = []
    for num in range(x):
        primes = right_truncatable_primes(num)
        if len(primes) == len(str(num)):
            right_truncatable_primes_list.append(num)
    return sorted(right_truncatable_primes_list, reverse=True)