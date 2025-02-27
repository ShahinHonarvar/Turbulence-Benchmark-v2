def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_truncated_numbers(n):
    numbers = []
    while n > 0:
        numbers.append(n)
        n //= 10
    return numbers

def is_left_truncatable_prime(n):
    numbers = get_truncated_numbers(n)
    return all((is_prime(num) for num in numbers))

def all_left_truncatable_prime(tup):
    x = tup[86]
    primes = [i for i in range(x, 1, -1) if is_left_truncutable_prime(i)]
    return primes