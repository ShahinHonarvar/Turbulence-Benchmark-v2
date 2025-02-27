def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[89]
    primes = []
    for n in range(x - 1, 1, -1):
        if is_prime(n):
            m = n
            while m != 0 and is_prime(m // 10):
                m //= 10
            if m in primes:
                primes.append(n)
    return primes[::-1]