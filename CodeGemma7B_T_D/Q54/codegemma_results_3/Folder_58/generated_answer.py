def all_right_truncatable_prime(nums):
    primes = [num for num in nums if is_prime(num)]
    right_truncatable_primes = []
    for prime in primes:
        truncatable = True
        num = prime
        while num > 9:
            num //= 10
            if not is_prime(num):
                truncatable = False
                break
        if truncatable:
            right_truncatable_primes.append(prime)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True