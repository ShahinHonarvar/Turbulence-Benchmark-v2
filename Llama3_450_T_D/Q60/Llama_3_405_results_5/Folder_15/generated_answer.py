def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[6]
    truncatable_primes = []
    for num in range(10, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        is_truncatable_prime = True
        for i in range(len(str_num)):
            truncated_num = int(str_num[i:])
            if not is_prime(truncated_num):
                is_truncatable_prime = False
                break
            if i > 0:
                truncated_num = int(str_num[:-i])
                if not is_prime(truncated_num):
                    is_truncatable_prime = False
                    break
        if is_truncatable_prime:
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)