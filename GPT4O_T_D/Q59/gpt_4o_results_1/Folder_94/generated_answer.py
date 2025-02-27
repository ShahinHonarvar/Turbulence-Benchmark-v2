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

def is_left_truncatable_prime(num):
    if '0' in str(num):
        return False
    return all((is_prime(int(str(num)[i:])) for i in range(len(str(num)))))

def all_left_truncatable_prime(numbers):
    x = numbers[43]
    return sorted([n for n in range(2, x) if is_left_truncatable_prime(n)])