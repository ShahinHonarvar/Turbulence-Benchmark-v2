def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[93]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' not in str(num):
            is_truncatable = True
            truncatable_num = num
            while len(str(truncatable_num)) > 1:
                truncatable_num = int(str(truncatable_num)[1:])
                if not is_prime(truncatable_num):
                    is_truncatable = False
                    break
            if is_truncatable and is_prime(num):
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)