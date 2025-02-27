def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    primes = []
    for num in range(x, 1, -1):
        if is_prime(num):
            n_str = str(num)
            if not '0' in n_str:
                while n_str:
                    n_str = n_str[1:-1]
                    if not is_prime(int(n_str)):
                        break
                    if len(n_str) == 2:
                        primes.append(num)
                        break
                else:
                    primes.append(num)
    return sorted(primes, reverse=True)