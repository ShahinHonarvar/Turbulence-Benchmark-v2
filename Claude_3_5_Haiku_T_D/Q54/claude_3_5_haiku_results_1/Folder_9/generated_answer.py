def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(input_tuple):
    x = input_tuple[29]
    right_truncatable_primes = []
    for num in range(x - 1, 1, -1):
        current_num = num
        is_truncatable = True
        while current_num > 0:
            if not is_prime(current_num):
                is_truncatable = False
                break
            current_num //= 10
        if is_truncatable and current_num == 0:
            right_truncatable_primes.append(num)
    return right_truncatable_primes