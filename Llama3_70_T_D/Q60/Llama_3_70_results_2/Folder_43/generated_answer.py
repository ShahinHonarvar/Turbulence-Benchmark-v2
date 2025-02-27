def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[89]
    truncatable_primes = []
    for n in range(10, x + 1):
        if '0' not in str(n) and is_prime(n):
            str_n = str(n)
            left_prime = True
            right_prime = True
            for i in range(1, len(str_n)):
                if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:-i])):
                    left_prime = False
                    right_prime = False
                    break
            if left_prime and right_prime:
                truncatable_primes.append(n)
    return sorted(truncatable_primes, reverse=True)