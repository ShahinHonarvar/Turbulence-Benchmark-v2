def all_left_right_truncatable_prime(t):
    x = t[31]
    primes = []
    for n in range(x, 1, -1):
        if all((n % i != 0 for i in range(2, int(n ** 0.5) + 1))) and n > 1 and ('0' not in str(n)):
            good = True
            for i in range(len(str(n)) - 1):
                if not all((int(str(n)[i + 1:j]) % i != 0 for i in range(2, int(int(str(n)[i + 1:j]) ** 0.5) + 1))) or int(str(n)[i + 1:j]) == 1 or '0' in str(int(str(n)[i + 1:j])):
                    good = False
                    break
            if good:
                primes.append(n)
    return primes