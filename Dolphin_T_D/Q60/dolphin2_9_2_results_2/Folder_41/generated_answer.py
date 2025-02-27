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

def is_truncatable(n):
    j = n
    while j > 9:
        if not is_prime(j):
            return False
        j = j // 10
    return True

def all_left_right_truncatable_prime(t):
    prime_numbers = []
    x = t[46]
    for i in range(2, x + 1):
        if is_truncatable(i):
            prime_numbers.append(i)
    return sorted(prime_numbers, reverse=True)