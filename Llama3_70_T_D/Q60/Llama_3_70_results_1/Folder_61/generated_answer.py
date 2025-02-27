def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(args):
    x = args[3]
    truncatable_primes = []
    for num in range(11, x + 1):
        if '0' not in str(num) and is_prime(num):
            str_num = str(num)
            is_truncatable_prime = True
            for i in range(1, len(str_num)):
                left_truncated = int(str_num[i:])
                right_truncated = int(str_num[:-i])
                if not (is_prime(left_truncated) and is_prime(right_truncated)):
                    is_truncatable_prime = False
                    break
            if is_truncatable_prime:
                truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)