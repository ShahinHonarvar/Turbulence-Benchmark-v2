def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[69]
    truncatable_primes = []
    for num in range(x, 0, -1):
        if is_prime(num):
            trunc = num
            while trunc > 9:
                trunc = int(str(trunc)[1:-1])
                if not is_prime(trunc):
                    break
            else:
                truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)