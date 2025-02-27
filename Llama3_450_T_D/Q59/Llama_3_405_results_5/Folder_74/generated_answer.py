def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[36]
    left_truncatable_primes = []
    for num in range(2, x):
        num_str = str(num)
        if '0' in num_str:
            continue
        all_primes = True
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])):
                all_primes = False
                break
        if all_primes:
            left_truncatable_primes.append(num)
    return left_truncatable_primes