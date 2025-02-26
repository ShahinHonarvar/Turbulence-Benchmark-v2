def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(inputs):
    x = inputs[35]
    truncatable_primes = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        is_left_right_truncatable = True
        for length in range(len(str(num)), 0, -1):
            left_trunc = int(str(num)[:length])
            right_trunc = int(str(num)[-length:])
            if not (is_prime(left_trunc) and is_prime(right_trunc)):
                is_left_right_truncatable = False
                break
        if is_left_right_truncatable and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)