def all_right_truncatable_prime(tuple_x):
    x = tuple_x[70]
    right_truncatable_primes = []
    for i in range(2, int(x ** 0.5) + 1):
        if is_prime(i):
            for j in range(1, 10):
                num = i
                for k in range(j):
                    num = num // 10
                if is_prime(num):
                    right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True