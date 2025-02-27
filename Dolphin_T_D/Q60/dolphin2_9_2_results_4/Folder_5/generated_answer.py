def all_left_right_truncatable_prime(numbers):
    x = numbers[55]
    trunc_primes = []
    for num in range(2, x + 1):
        trunc_nums = [int(str(num)[i:j]) for i in range(len(str(num))) for j in range(i + 1, len(str(num)) + 1)]
        if all((c in '123456789' for c in str(num))) and all((is_prime(i) for i in trunc_nums)):
            trunc_primes.append(num)
    return trunc_primes

def is_prime(n):
    if n < 2 or 2 % n == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True