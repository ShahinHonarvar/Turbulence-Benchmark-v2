def all_left_truncatable_prime(t):
    x = t[89]
    prime = [True] * (x + 1)
    prime[0] = prime[1] = False
    for i in range(2, int(x ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, x + 1, i):
                prime[j] = False
    result = []
    for p in range(2, x):
        if prime[p] and (not '0' in str(p)):
            temp = p
            while temp > 0:
                if not prime[temp]:
                    break
                temp //= 10
            else:
                result.append(p)
    return result[::-1]