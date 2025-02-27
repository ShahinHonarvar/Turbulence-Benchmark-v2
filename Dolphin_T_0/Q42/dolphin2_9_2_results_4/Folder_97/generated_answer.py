def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def prime_factors(numbers):
    number = numbers[132]
    prime_set = set()
    for i in range(2, number + 1):
        if is_prime(i) and number % i == 0:
            prime_set.add(i)
        if i * i > number:
            break
    return prime_set