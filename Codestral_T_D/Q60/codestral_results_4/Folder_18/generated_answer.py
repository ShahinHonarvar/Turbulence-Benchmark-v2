def all_left_right_truncatable_prime(numbers):
    x = numbers[429]
    trunc_primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        if all((is_prime(int(str(num)[:i])) and is_prime(int(str(num)[i:])) for i in range(1, len(str(num))))):
            trunc_primes.append(num)
    return sorted(trunc_primes, reverse=True)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True