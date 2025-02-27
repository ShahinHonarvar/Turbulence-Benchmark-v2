def all_right_truncatable_prime(numbers):
    x = numbers[41]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)

def is_right_truncatable_prime(num):
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
    while num > 0:
        if num < 10 and num != 2 and (num != 3) and (num != 5) and (num != 7):
            return False
        if num >= 10 and (num % 2 == 0 or num % 5 == 0):
            return False
        if num > 10:
            num = int(str(num)[:-1])
        else:
            return True