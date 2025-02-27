def all_left_truncatable_prime(numbers):
    x = numbers[370]
    primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            str_i = str(i)
            is_left_truncatable = True
            for k in range(1, len(str_i)):
                if not is_prime(int(str_i[k:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True