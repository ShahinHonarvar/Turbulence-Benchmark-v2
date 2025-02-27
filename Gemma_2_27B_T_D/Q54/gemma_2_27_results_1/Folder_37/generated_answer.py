def all_right_truncatable_prime(numbers):
    x = numbers[35]
    primes = []
    for num in range(2, x):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            truncatable = True
            n = str(num)
            while len(n) > 1:
                n = n[:-1]
                if not is_prime(int(n)):
                    truncatable = False
                    break
            if truncatable:
                primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True