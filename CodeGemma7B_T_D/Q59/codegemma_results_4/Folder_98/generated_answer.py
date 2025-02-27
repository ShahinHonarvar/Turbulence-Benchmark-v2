def all_left_truncatable_prime(tup):
    x = tup[8]
    prime = [False] * (x + 1)
    prime[0] = prime[1] = True
    for i in range(2, x + 1):
        if not prime[i]:
            j = 2
            k = i * j
            while k <= x:
                prime[k] = True
                j += 1
                k = i * j
    plist = [i for i in range(x + 1) if not prime[i]]
    return sorted([i for i in plist if str(i) not in '0' and all((prime[int(str(i)[j:])] for j in range(1, len(str(i)))))], reverse=True)