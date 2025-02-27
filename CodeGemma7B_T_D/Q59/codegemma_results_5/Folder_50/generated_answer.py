def all_left_truncatable_prime(t):
    x = t[57]
    prime = [True] * (x + 1)
    prime[0], prime[1] = (False, False)
    prime_list = []
    for i in range(2, int(x ** 0.5) + 1):
        if prime[i]:
            prime_list.append(i)
            for j in range(i * i, x + 1, i):
                prime[j] = False
    prime_list.reverse()
    ans = []
    for p in prime_list:
        if str(p) not in '0' and all((str(p)[k:] in prime_list for k in range(len(str(p)) - 1))):
            ans.append(p)
    return ans