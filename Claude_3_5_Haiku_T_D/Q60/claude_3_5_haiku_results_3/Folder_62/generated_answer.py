def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[70]
    truncatable_primes = []
    for num in range(10, x + 1):
        if '0' in str(num):
            continue
        if is_prime(num):
            is_truncatable = True
            left_str = str(num)
            while len(left_str) > 1:
                left_str = left_str[1:]
                if not is_prime(int(left_str)):
                    is_truncatable = False
                    break
            right_str = str(num)
            while len(right_str) > 1:
                right_str = right_str[:-1]
                if not is_prime(int(right_str)):
                    is_truncatable = False
                    break
            if is_truncatable:
                truncatable_primes.append(num)
    return sorted(truncatable_primes)