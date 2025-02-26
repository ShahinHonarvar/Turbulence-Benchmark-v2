def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[10]
    truncatable_primes = []
    for num in range(x, 11, -1):
        if '0' not in str(num):
            is_truncatable = True
            left_trunc = num
            while len(str(left_trunc)) > 1:
                left_trunc = int(str(left_trunc)[1:])
                if not is_prime(left_trunc):
                    is_truncatable = False
                    break
            right_trunc = num
            while len(str(right_trunc)) > 1:
                right_trunc = int(str(right_trunc)[:-1])
                if not is_prime(right_trunc):
                    is_truncatable = False
                    break
            if is_truncatable and is_prime(num):
                truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)