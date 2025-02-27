def all_left_truncatable_prime(tup):

    def is_left_truncatable_prime(n):
        if n < 2:
            return False
        n = list(str(n))
        while n:
            if n[0] == '0':
                return False
            if not isprime(int(''.join(n))):
                return False
            n.pop(0)
        return True

    def isprime(n):
        if n == 2:
            return True
        if n % 2 == 0 or n == 1:
            return False
        p = 3
        while p * p <= n:
            if n % p == 0:
                return False
            p += 2
        return True
    prime_list = []
    x = tup[14]
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            prime_list.append(i)
    return sorted(prime_list)