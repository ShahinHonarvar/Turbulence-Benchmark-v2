def all_left_truncatable_prime(tupl):

    def check_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = tupl[70]
    left_trim_primes = [2, 3, 5, 7]
    i = 10
    while i <= x:
        d = [int(s) for s in str(i)]
        if 0 not in d:
            if check_prime(i):
                is_trunc = True
                for j in range(len(d)):
                    if not check_prime(int(''.join([str(k) for k in d[j:]]))):
                        is_trunc = False
                        break
                if is_trunc:
                    left_trim_primes.append(i)
        i += 1
    return sorted(left_trim_primes)