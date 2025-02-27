def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[87]
    truncatable_primes = set()
    for num in range(10, x):
        if is_prime(num):
            truncatable = True
            temp = num
            while temp >= 10:
                temp = int(str(temp)[:-1])
                if not is_prime(temp):
                    truncatable = False
                    break
            if truncatable:
                truncatable_primes.add(num)
    return sorted(list(truncatable_primes))