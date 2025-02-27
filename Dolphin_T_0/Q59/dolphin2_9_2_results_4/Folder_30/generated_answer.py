def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[37]
    left_truncatable_primes = []
    for num in range(x - 1, 1, -1):
        if is_prime(num) and '0' not in str(num):
            trunc = num
            while trunc > 1:
                if not is_prime(trunc):
                    break
                trunc = int(str(trunc)[1:])
            else:
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)