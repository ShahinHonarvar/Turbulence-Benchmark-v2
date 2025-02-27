def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n ** 0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[69]
    right_truncatable_primes = []
    for i in range(10, x):
        str_i = str(i)
        if is_prime(i):
            truncatable = True
            for j in range(len(str_i)):
                if not is_prime(int(str_i[:-j - 1])):
                    truncatable = False
                    break
            if truncatable:
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)