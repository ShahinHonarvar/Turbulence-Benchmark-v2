def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[30]
    truncatable_primes = set()
    for num in range(11, x + 1):
        num_str = str(num)
        if '0' in num_str:
            continue
        truncatable = True
        for i in range(len(num_str)):
            left_trunc = int(num_str[i:])
            right_trunc = int(num_str[:-i - 1])
            if left_trunc != num and (not is_prime(left_trunc)):
                truncatable = False
                break
            if right_trunc != num and (not is_prime(right_trunc)):
                truncatable = False
                break
        if truncatable and is_prime(num):
            truncatable_primes.add(num)
    return sorted(list(truncatable_primes))