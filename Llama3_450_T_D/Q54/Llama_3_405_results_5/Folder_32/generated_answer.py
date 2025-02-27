def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[42]
    right_truncatable_primes = []
    for num in range(2, x):
        num_str = str(num)
        if is_prime(num):
            truncatable = True
            for i in range(len(num_str) - 1, 0, -1):
                trunc_num = int(num_str[:i])
                if not is_prime(trunc_num):
                    truncatable = False
                    break
            if truncatable:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)