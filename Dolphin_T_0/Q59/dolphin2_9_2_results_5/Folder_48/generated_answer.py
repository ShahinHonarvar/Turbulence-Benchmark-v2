def all_left_truncatable_prime(t):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    x = t[835]
    T = [2]
    left_truncatable_primes = [2]
    for i in range(3, x + 1):
        if is_prime(i) and str(i).count('0') == 0:
            T.append(i)
        for j in range(len(T) - 1, -1, -1):
            if is_prime(T[j]) and str(T[j]).count('0') == 0:
                T.append(T[j] * 10 + i % 10)
                if T[-1] < x:
                    left_truncatable_primes.append(T[-1])
    return sorted(list(set(left_truncatable_primes)))