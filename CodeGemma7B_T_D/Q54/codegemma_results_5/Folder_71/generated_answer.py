def all_right_truncatable_prime(t):
    x = t[22]
    if x <= 3 or x % 2 == 0 or x % 3 == 0:
        return []
    prime = [True] * (x + 1)
    for i in range(5, x + 1, 6):
        if prime[i]:
            prime[i * i:x + 1:i] = [False] * ((x - i * i) // i + 1)
    ans = []
    for i in range(x - 1, 1, -1):
        if prime[i]:
            if all((prime[int(str(i)[:-j])] for j in range(1, len(str(i))))):
                ans.append(i)
    return sorted(ans, reverse=True)