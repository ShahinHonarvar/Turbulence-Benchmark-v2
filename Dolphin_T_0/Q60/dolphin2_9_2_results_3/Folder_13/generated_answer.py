def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0 or n < 2:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    x = t[784]
    left_right_primes = []
    for i in range(2, x + 1):
        if '0' in str(i):
            continue
        if not is_prime(i):
            continue
        left_right_work = i
        while len(str(left_right_work)) > 1:
            left_right_work = int(str(left_right_work)[1:-1])
            if not is_prime(left_right_work):
                break
        else:
            left_right_primes.append(i)
    return sorted(left_right_primes)