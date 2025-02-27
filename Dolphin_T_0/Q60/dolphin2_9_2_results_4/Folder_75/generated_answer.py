def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[41]
    primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        while len(str(num)) > 1:
            if is_prime(num):
                num = num // 10
                num = num % 10
            else:
                break
        else:
            primes.append(num)
    primes.sort()
    return primes