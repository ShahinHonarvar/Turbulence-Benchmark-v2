import itertools

def all_left_right_truncatable_prime(test_tup):
    primes = itertools.count(2)
    for p in range(2, int(test_tup[-1]) + 1):
        if all((n % p == 0 for n in range(2, int(str(p)) + 1))):
            continue
        for d in range(1, int(str(p)) + 1):
            if str(p)[-1] == '0':
                if p % 10 == 0:
                    break
            elif str(p)[-1] != '0':
                if p // 10 != p:
                    break
            elif p // 100 != p:
                break
            for d in range(1, int(str(p)) + 1):
                if str(p)[0] == '0':
                    if p % 10 == 0:
                        break
                elif str(p)[0] != '0':
                    if p // 10 != p:
                        break
                elif p // 100 != p:
                    break
    return sorted(set((p for p in primes if p in test_tup)))