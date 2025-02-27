def all_right_truncatable_prime(numbers):
    x = numbers[14]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            right_truncatable_primes.append(num)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes

def is_right_truncatable_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    while num > 0:
        if num < 10 and num not in [2, 3, 5, 7]:
            return False
        if num >= 10 and num % 10 not in [1, 3, 7, 9]:
            return False
        num //= 10
    return True