def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[84]
    truncatable_primes = set()
    for num in range(10, x):
        str_num = str(num)
        if all((is_prime(int(str_num[:i + 1])) for i in range(len(str_num)))):
            truncatable_primes.add(num)
    return sorted(truncatable_primes, reverse=True)