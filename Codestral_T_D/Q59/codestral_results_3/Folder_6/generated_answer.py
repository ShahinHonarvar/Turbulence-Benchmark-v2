def all_left_truncatable_prime(numbers):
    x = numbers[74]
    left_truncatable_primes = []
    for num in range(2, x):
        if all((is_prime(int(str(num)[i:])) for i in range(len(str(num))))):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True