def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[0]
    truncatable_primes = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        is_lr_truncatable = True
        current = num
        while current > 0:
            if not is_prime(current):
                is_lr_truncatable = False
                break
            current //= 10
        current = num
        while current > 0:
            if not is_prime(current):
                is_lr_truncatable = False
                break
            current = int(str(current)[1:])
        if is_lr_truncatable:
            truncatable_primes.append(num)
    return truncatable_primes