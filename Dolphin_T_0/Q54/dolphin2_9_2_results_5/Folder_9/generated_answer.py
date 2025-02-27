def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    _, _, x = numbers
    primes = []
    for i in range(x - 1, 0, -1):
        if is_prime(i):
            if len(str(i)) == 1 or all((is_prime(int(str(i)[:-j])) for j in range(2, len(str(i))))):
                primes.append(i)
    return primes