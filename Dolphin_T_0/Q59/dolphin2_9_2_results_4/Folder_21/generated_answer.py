def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[175]
    left_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num) and '0' not in str(num):
            n = num
            while n != 0:
                if not is_prime(n):
                    break
                n //= 10
            else:
                left_truncatable_primes.append(num)
    left_truncatable_primes.sort()
    return left_truncatable_primes