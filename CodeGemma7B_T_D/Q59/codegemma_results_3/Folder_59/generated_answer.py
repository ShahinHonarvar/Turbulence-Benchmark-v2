def all_left_truncatable_prime(a):

    def isprime(x):
        if x % 2 == 0:
            return False
        for i in range(3, int(x ** 0.5) + 1, 2):
            if x % i == 0:
                return False
        return True

    def is_truncatable(x):
        if '0' in str(x):
            return False
        for i in range(1, len(str(x))):
            if not isprime(int(str(x)[:i])):
                return False
        return True
    prime = [i for i in a if isprime(i)]
    prime.sort(reverse=True)
    left_trunc = []
    for i in prime:
        if is_truncatable(i):
            left_trunc.append(i)
    return left_trunc