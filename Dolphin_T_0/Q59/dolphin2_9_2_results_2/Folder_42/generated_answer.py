def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(PayLoad):
    x = PayLoad[64]
    primes = [2, 3, 5, 7]
    for num in range(10, x + 1):
        if is_prime(num):
            is_truncatable = True
            for digit in str(num)[1:-1]:
                if not is_prime(int(digit)):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(num)
    primes.sort(reverse=True)
    return primes