def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[25]
    primes = []
    for num in range(x, 0, -1):
        if '0' not in str(num) and is_prime(num):
            trunc = num
            while trunc > 1:
                trunc = int(str(trunc)[1:-1])
                if not is_prime(trunc):
                    break
            else:
                primes.append(num)
    primes.sort(reverse=True)
    return primes