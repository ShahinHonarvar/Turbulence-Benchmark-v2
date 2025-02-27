def all_left_truncatable_prime(tup):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    left_truncatable_primes = []
    for num in tup:
        if num <= 1:
            continue
        if not str(num).startswith('0') and is_prime(num):
            for i in range(1, len(str(num))):
                truncated_num = int(str(num)[i:])
                if not is_prime(truncated_num):
                    break
            else:
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)