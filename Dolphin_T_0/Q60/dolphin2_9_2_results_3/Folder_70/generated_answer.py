def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[433]
    primes = []
    for num in range(x, 0, -1):
        if is_prime(num) and str(num).count('0') == 0:
            trunc = {int(str(num)[i:j]) for i in range(len(str(num))) for j in range(i + 1, len(str(num)) + 1)}
            if all((is_prime(i) for i in trunc)):
                primes.append(num)
    return sorted(primes, reverse=True)