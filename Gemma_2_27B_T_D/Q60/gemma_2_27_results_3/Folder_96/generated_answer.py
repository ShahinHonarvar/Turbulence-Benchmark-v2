def all_left_right_truncatable_prime(numbers):
    x = numbers[29]
    primes = []
    for num in range(2, x + 1):
        if all((int(str(num)[:i]) in [2, 3, 5, 7] or ((int(str(num)[:i]) > 10 and is_prime(int(str(num)[:i]))) and int(str(num)[i:]) in [2, 3, 5, 7]) or (int(str(num)[i:]) > 10 and is_prime(int(str(num)[i:]))) for i in range(1, len(str(num))))) and is_prime(num):
            primes.append(num)
    return sorted(primes)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True