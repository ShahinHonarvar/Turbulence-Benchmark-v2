def prime_factors(numbers):
    prime_factors_set = set()
    for num in numbers[:20]:
        if num > 1:
            for i in range(2, num + 1):
                if num % i == 0:
                    if is_prime(i):
                        prime_factors_set.add(i)
                        break
    return prime_factors_set

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True