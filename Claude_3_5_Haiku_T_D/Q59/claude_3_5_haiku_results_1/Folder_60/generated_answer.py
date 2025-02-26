def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[87]
    left_truncatable_primes = []
    for n in range(2, x):
        if is_prime(n):
            str_n = str(n)
            is_left_truncatable = True
            for i in range(1, len(str_n)):
                if not is_prime(int(str_n[i:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable and '0' not in str_n:
                left_truncatable_primes.append(n)
    return sorted(left_truncatable_primes)