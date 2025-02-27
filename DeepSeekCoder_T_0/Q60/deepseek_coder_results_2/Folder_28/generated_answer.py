def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[19]
    primes = set()

    def generate_lr_truncatable_primes(num_str):
        if len(num_str) > len(str(x)) or int(num_str) > x:
            return
        if is_prime(int(num_str)):
            primes.add(int(num_str))
            for d in '123456789':
                generate_lr_truncatable_primes(d + num_str + d)
    for d in '123456789':
        generate_lr_truncatable_primes(d)
    return sorted(filter(lambda p: p <= x, primes))