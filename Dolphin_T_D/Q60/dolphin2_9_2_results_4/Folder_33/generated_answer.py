def all_left_right_truncatable_prime(x):

    def check_primes_lr(n):
        i = 1
        while i < len(n):
            if n[i] == 0:
                return False
            i += 1
        i = 1
        while i < len(n):
            if is_prime(n[:i]):
                i += 1
            else:
                return False
        i = 1
        while i < len(n):
            if is_prime(n[-i:]):
                i += 1
            else:
                return False
        return True

    def is_prime(n):
        if n[0] == '0' or n[-1] == '0':
            return False
        if n[0] == '1' or n[-1] == '1':
            n = int(n)
        else:
            n = eval(n)
        if n == 1 or n == 0:
            return False
        if n < 4:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True
    n = len(str(x))
    digits = [i for i in range(10)]
    prime_list = [i for i in range(2, x + 1) if is_prime(i)]
    all_lr_primes = [i for i in prime_list if check_primes_lr(str(i))]
    lr_primes_descending = all_lr_primes[::-1]
    return lr_primes_descending