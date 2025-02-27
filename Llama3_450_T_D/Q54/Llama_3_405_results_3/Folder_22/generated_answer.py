def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[85]
    right_truncatable_primes = set()
    for num in range(10, x):
        num_str = str(num)
        for i in range(len(num_str)):
            trunc_num = int(num_str[:len(num_str) - i])
            if not is_prime(trunc_num):
                break
        else:
            right_truncatable_primes.add(num)
    return sorted(list(right_truncatable_primes))