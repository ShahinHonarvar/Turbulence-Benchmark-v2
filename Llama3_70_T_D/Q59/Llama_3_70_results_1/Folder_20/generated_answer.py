def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[100]
    left_truncatable_primes = []
    for num in numbers:
        if num < x and '0' not in str(num):
            is_lt_prime = True
            for i in range(1, len(str(num))):
                if not is_prime(int(str(num)[i:])):
                    is_lt_prime = False
                    break
            if is_lt_prime and is_prime(num):
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)