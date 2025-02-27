from itertools import count

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_right_truncatable_primes():
    for i in count(10):
        if is_prime(i):
            yield i
            num = i
            while num > 0:
                num = num // 10 * 10 + num % 10
                if is_prime(num):
                    yield num

def all_right_truncatable_prime(t):
    x = tuple(t)[100]
    result = []
    for num in generate_right_truncatable_primes():
        if num < x:
            result.append(num)
        else:
            break
    return sorted(result)