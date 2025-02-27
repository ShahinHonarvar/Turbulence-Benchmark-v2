def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    primes = []
    for num in range(x, 0, -1):
        str_num = str(num)
        if '0' not in str_num:
            is_left_right_truncatable = True
            truncated = str_num[1:-1]
            while truncated and is_prime(int(truncated)):
                truncated = truncated[1:-1]
                if len(truncated) == 1:
                    is_left_right_truncatable = False
                    break
            if is_left_right_truncatable:
                primes.append(num)
    return sorted(primes, reverse=True)