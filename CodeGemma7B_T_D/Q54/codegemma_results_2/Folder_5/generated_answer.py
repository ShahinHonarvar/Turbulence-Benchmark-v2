def all_right_truncatable_prime(t):
    x = t[55]
    digprime = defaultdict(int)
    for digit in range(10):
        digprime[digit] = 2
    prime = [2, 3, 5, 7, 11, 13, 17, 19]
    for i in prime:
        n = i
        for j in range(1, int(x.log10()) + 1):
            for digit in str(n)[j:]:
                digprime[int(digit)] -= 1
            n = n // 10
        if all([i == 0 for i in digprime.values()]):
            return sorted(prime[:prime.index(i) + 1])
    return []