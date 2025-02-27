def all_right_truncatable_prime(x):
    truncatable_primes = []
    if is_prime(x[-1]):
        for i in range(len(x) - 2):
            num = int(''.join((str(n) for n in x[i:len(x) - i])))
            if is_prime(num):
                truncatable_primes.append(num)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes