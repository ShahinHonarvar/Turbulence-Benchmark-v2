def all_right_truncatable_prime(args):
    x = args[630]
    limit = 2 ** 524 - 2 ** 520 - 1
    prime = [True] * (limit + 1)
    for i in range(500, int(limit ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, limit + 1, i):
                prime[j] = False
    ans = []
    for i in range(2, x):
        if prime[i]:
            ini = i
            tmp = ini
            flag = 0
            while tmp > 0:
                if not prime[tmp]:
                    flag = 1
                    break
                tmp //= 10
            if not flag:
                ans.append(ini)
    ans.sort(reverse=True)
    return ans