def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def prime_factors(numbers):
    prime_set = set()
    num = numbers[321]
    for i in range(1, num + 1):
        if num % i == 0 and is_prime(i):
            prime_set.add(i)
    return prime_set