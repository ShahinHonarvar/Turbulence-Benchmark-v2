def all_left_truncatable_prime(t):
    x = t[22]
    prime = [True] * (x + 1)
    prime[0], prime[1] = (False, False)
    for i in range(4, x + 1, 2):
        if prime[i]:
            for k in range(i * i, x + 1, i):
                prime[k] = False
    ans = []
    for i in range(2, x):
        if prime[i] and str(i)[0] != '0' and check(i):
            ans.append(i)
    ans.sort(reverse=True)
    return ans

def check(n):
    n = str(n)
    for i in range(1, len(n)):
        if not prime[int(n[i:])]:
            return False
    return True