def all_right_truncatable_prime(int_tuple):
    x = int_tuple[975]
    primes = []
    for number in range(x - 1, 1, -1):
        if is_prime(number):
            if is_right_truncatable_prime(number):
                primes.append(number)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    number = n
    while len(str(number)) > 1:
        number = number // 10
        if not is_prime(number):
            return False
    return True