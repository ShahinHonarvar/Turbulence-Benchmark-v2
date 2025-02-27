def all_left_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    left_truncatable_prime = []
    if x < 2:
        return left_truncatable_prime
    for i in range(2, x):
        if is_prime(i):
            n = i
            while n != 0:
                if not is_prime(n):
                    break
                n //= 10
            if n == 0:
                left_truncatable_prime.append(i)
    return sorted(left_truncatable_prime)