def all_left_truncatable_prime(t):
    prime_numbers = set()
    x = t[39]
    previous_number = x - 1
    while True:
        if is_prime(previous_number):
            if check_truncatable_prime(previous_number):
                prime_numbers.add(previous_number)
        if len(prime_numbers) > 30:
            break
        previous_number -= 1
    return sorted(list(prime_numbers), reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    p = 5
    while p * p <= n:
        if n % p == 0 or n % (p + 2) == 0:
            return False
        p += 6
    return True

def check_truncatable_prime(n):
    while n != 0:
        if not is_prime(n):
            return False
        n = int(n / 10)
    return True