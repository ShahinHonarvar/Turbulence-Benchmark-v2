def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(args):
    limit = args[0]
    left_truncatable_primes = []
    for num in range(2, limit):
        if '0' not in str(num):
            is_left_truncatable_prime = True
            for i in range(1, len(str(num))):
                trunc_num = int(str(num)[i:])
                if not is_prime(trunc_num):
                    is_left_truncatable_prime = False
                    break
            if is_left_truncatable_prime and is_prime(num):
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)