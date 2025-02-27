def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[1]
    primes = [2, 3, 5, 7]
    candidates = [p for p in primes if p <= x]
    found = []
    while candidates:
        new_candidates = []
        for c in candidates:
            for i in range(1, 10):
                num = i * 10 ** len(str(c)) + c
                if num > x:
                    continue
                if is_prime(num):
                    new_candidates.append(num)
            for i in range(1, 10):
                num = c * 10 + i
                if num > x:
                    continue
                if is_prime(num):
                    new_candidates.append(num)
        candidates = new_candidates
        found.extend(candidates)
    found = [p for p in found if p not in [23, 37, 53, 73]]
    return sorted(set(found), reverse=True)