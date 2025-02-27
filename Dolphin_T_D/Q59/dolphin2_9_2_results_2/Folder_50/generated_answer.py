def all_left_truncatable_prime(args):

    def is_prime(n):
        if n % 2 == 0 and n > 2:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    x = args[57]
    left_truncatable_primes = []
    for num in range(x - 1, 1, -1):
        n = str(num)
        if '0' in n:
            continue
        while n:
            if not is_prime(int(n)):
                break
            n = n[1:]
        if n == '':
            left_truncatable_primes.append(num)
    return left_truncatable_primes