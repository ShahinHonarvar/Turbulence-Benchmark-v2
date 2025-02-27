def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[758]
    left_right_truncatable_primes = []
    for num in range(x, 1, -1):
        if '0' not in str(num) and is_prime(num):
            trunc = num
            while trunc > 9:
                if not is_prime(trunc):
                    break
                trunc = int(str(trunc)[1:-1])
                if trunc <= 1:
                    break
            else:
                left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)