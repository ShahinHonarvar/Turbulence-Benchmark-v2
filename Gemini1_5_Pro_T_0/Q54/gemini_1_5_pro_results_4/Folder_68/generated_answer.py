def all_right_truncatable_prime(numbers):
    x = numbers[1]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes

def is_right_truncatable_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3 or num == 5 or (num == 7):
        return True
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or (num % 7 == 0):
        return False
    for i in range(11, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    while num > 0:
        if num == 2 or num == 3 or num == 5 or (num == 7):
            return True
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or (num % 7 == 0):
            return False
        for i in range(11, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        num = num // 10
    return True