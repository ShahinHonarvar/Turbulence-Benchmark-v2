def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def right_truncatable_prime(index, x):
    if index == 0:
        return []
    number = ''.join((str(x)[i] for i in range(index)))
    if int(number) < 2:
        return []
    if int(number) == 2:
        return ['2']
    if int(number) % 2 == 0:
        return []
    primes = right_truncatable_prime(index - 1, x)
    if all((int(number) % prime != 0 for prime in primes)):
        return primes + [number]
    return primes

def all_right_truncatable_prime(nums):
    x = nums[8]
    numbers = [str(n) for n in range(2, x + 1)]
    return sorted([n for n in numbers if is_prime(int(n)) and right_truncatable_prime(len(n) - 1, int(n)) == list(n)], reverse=True)