def all_left_truncatable_prime(t):
    x = t[31]
    nums = [i for i in range(2, x) if '0' not in str(i)]
    primes = []
    for n in nums:
        if is_prime(n):
            primer = True
            for j in range(1, len(str(n))):
                if not is_prime(int(str(n)[:j])):
                    primer = False
                    break
            if primer:
                primes.append(n)
    p = len(primes)
    while p > 0 and primes[p - 1] >= x:
        primes.pop(p - 1)
        p -= 1
    return sorted(primes, reverse=True)

def is_prime(n):
    a = 2
    while a * a <= n:
        if n % a == 0:
            return False
        a += 1
    return True