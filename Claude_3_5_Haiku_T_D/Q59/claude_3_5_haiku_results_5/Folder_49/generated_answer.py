def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(input_tuple):
    x = input_tuple[14]
    truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            str_num = str(num)
            is_left_truncatable = True
            for i in range(1, len(str_num)):
                truncated_num = int(str_num[i:])
                if not is_prime(truncated_num):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                truncatable_primes.append(num)
    return sorted(truncatable_primes)