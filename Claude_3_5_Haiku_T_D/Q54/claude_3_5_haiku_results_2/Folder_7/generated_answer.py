def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[803]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            temp = num
            is_truncatable = True
            while temp > 0:
                temp //= 10
                if temp > 0 and (not is_prime(temp)):
                    is_truncatable = False
                    break
            if is_truncatable:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)