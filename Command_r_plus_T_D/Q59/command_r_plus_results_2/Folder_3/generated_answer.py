def all_left_truncatable_prime(limit_tup):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_left_truncatable_primes(limit):
        primes = []
        for i in range(limit):
            if i == 0 or str(i).count('0') > 0:
                continue
            is_truncatable = True
            temp = i
            while temp:
                if not is_prime(temp):
                    is_truncatable = False
                    break
                temp //= 10
            if is_truncatable:
                primes.append(i)
        return primes
    limit = limit_tup[100]
    return generate_left_truncatable_primes(limit)