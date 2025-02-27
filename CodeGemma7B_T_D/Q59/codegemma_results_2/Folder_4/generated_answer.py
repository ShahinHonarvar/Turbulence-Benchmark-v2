def all_left_truncatable_prime(args):
    x = args[96]
    prime = [True] * (x // 2 + 2)
    prime[0] = prime[1] = False
    for i in range(2, int(x ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, x + 1, i):
                prime[j] = False
    result = []
    for i in range(2, x):
        if prime[i]:
            if '0' not in str(i):
                is_truncatable = True
                temp = i
                while temp > 0:
                    if not prime[temp]:
                        is_truncatable = False
                        break
                    temp //= 10
                if is_truncatable:
                    result.append(i)
    return sorted(result, reverse=True)