def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[54]
    left_truncatable_primes = []
    for num in range(x - 1, 1, -1):
        if '0' not in str(num):
            is_truncatable = all((is_prime(int(str(num)[i:])) for i in range(len(str(num)))))
            if is_truncatable:
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)