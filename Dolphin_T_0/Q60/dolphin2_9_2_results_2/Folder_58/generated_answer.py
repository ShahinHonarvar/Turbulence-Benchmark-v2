def all_left_right_truncatable_prime(integer_tuple):
    x = integer_tuple[975]
    primes = all_primes_below(x)
    truncatables = []
    for prime in primes:
        if is_left_and_right_truncatable(prime):
            truncatables.append(prime)
    truncatables.sort(reverse=True)
    return truncatables

def all_primes_below(number):
    prime = [True] * (number + 1)
    p = 2
    while p * p <= number:
        if prime[p] == True:
            for i in range(p * p, number + 1, p):
                prime[i] = False
        p += 1
    primes = [p for p in range(2, number + 1) if prime[p]]
    return primes

def is_left_and_right_truncatable(number):
    if '0' in str(number):
        return False
    while number > 9:
        if not is_prime(number):
            return False
        number = number // 10
    return is_prime(number)

def is_prime(number):
    if number == 0 or number == 1:
        return False
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True