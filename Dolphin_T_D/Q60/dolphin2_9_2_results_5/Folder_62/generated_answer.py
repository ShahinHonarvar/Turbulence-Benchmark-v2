def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    leftright_primes = []
    x = t[70]
    for i in range(2, x + 1):
        if '0' in str(i):
            continue
        elif is_prime(i):
            leftright = True
            for j in range(1, len(str(i)) - 1):
                trimmed = int(str(i)[j:-j])
                if not is_prime(trimmed):
                    leftright = False
                    break
            if leftright:
                leftright_primes.append(i)
    return sorted(leftright_primes)