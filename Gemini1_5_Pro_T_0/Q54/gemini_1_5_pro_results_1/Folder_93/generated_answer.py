def all_right_truncatable_prime(numbers):
    x = numbers[11]
    right_truncatable_primes = []
    for number in range(2, x):
        if is_right_truncatable_prime(number):
            right_truncatable_primes.append(number)
    return sorted(right_truncatable_primes)

def is_right_truncatable_prime(number):
    if number < 2:
        return False
    number_str = str(number)
    for i in range(len(number_str)):
        if not is_prime(int(number_str[i:])):
            return False
    return True

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True