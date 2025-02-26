def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[97]
    left_truncatable_primes = []
    for n in range(x - 1, 1, -1):
        if '0' not in str(n):
            is_left_truncatable = True
            temp = n
            while len(str(temp)) > 1:
                temp = int(str(temp)[1:])
                if not is_prime(temp):
                    is_left_truncatable = False
                    break
            if is_left_truncatable and is_prime(n):
                left_truncatable_primes.append(n)
    return sorted(left_truncatable_primes, reverse=True)