def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[945]
    right_truncatable_primes = []
    for num in range(2, x):
        num_str = str(num)
        is_right_truncatable_prime = True
        for i in range(len(num_str)):
            trunc_num = int(num_str[:len(num_str) - i])
            if not is_prime(trunc_num):
                is_right_truncatable_prime = False
                break
        if is_right_truncatable_prime:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)