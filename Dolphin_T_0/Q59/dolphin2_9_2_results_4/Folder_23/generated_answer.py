def all_left_truncatable_prime(t):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    x = t[77]
    left_truncatable_primes = []
    for i in reversed(range(2, x)):
        if is_prime(i) and (not '0' in str(i)):
            for j in str(i):
                if i != int(j) and (not is_prime(int(str(i).replace(j, '')))):
                    break
            else:
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)