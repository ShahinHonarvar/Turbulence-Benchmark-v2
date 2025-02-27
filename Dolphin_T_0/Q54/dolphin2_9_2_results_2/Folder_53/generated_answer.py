def all_right_truncatable_prime(numbers):
    x = numbers[86]
    primes = [2, 3, 5, 7]
    for num in range(11, x):
        if is_prime(num):
            is_truncatable = True
            for digit in range(len(str(num)) - 1):
                if not is_prime(int(str(num)[-digit - 1:])):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True