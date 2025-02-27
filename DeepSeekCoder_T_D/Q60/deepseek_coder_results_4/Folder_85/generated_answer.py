def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[94]
    primes = set()

    def generate_lr_truncatable_primes(num_str):
        if num_str and int(num_str) <= x:
            if is_prime(int(num_str)):
                primes.add(int(num_str))
                for i in range(1, 10):
                    new_num_str = str(i) + num_str + str(i)
                    if is_prime(int(new_num_str)):
                        generate_lr_truncatable_primes(new_num_str)
    for i in range(2, 10):
        generate_lr_truncatable_primes(str(i))
    return sorted(primes)