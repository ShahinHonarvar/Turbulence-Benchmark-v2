def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[88]
    primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        if is_prime(num):
            n = num
            while n > 9:
                if not is_prime(n):
                    break
                n //= 10
            else:
                primes.append(num)
    return sorted(primes, reverse=True)