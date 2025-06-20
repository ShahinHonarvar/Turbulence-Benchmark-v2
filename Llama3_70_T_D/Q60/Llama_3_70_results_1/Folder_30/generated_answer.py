def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(args):
    x = args[37]
    truncatable_primes = []
    for num in range(11, x + 1):
        if '0' in str(num):
            continue
        num_str = str(num)
        if is_prime(num):
            for i in range(1, len(num_str)):
                if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:-i])):
                    break
            else:
                truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)