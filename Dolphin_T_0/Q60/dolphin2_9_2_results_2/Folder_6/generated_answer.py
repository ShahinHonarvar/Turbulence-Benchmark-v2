def all_left_right_truncatable_prime(tup):
    num = tuple[74]
    primes = [i for i in range(2, num + 1) if all((i % n != 0 for n in range(2, i)))]
    truncatables = []
    for p in primes:
        s = str(p)
        while len(s) > 1:
            if len(s) == 2 and int(s) not in primes:
                break
            else:
                t = int(s[1:-1])
                if t in primes:
                    if s[0] != '0' and s[-1] != '0' and (t not in truncatables):
                        truncatables.append(t)
                    s = str(t)
    return sorted(truncatables)