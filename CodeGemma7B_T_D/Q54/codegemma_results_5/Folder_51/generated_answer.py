def all_right_truncatable_prime(arg):
    x = arg[54]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            str_i = str(i)
            truncatable = True
            for j in range(len(str_i) - 1):
                str_i = str_i[:j] + str_i[j + 1:]
                if not is_prime(int(str_i)):
                    truncatable = False
                    break
            if truncatable:
                right_truncatable_primes.append(i)
    right_truncatable_primes.sort()
    return right_truncatable_primes

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True