def all_left_truncatable_prime(args):
    x = args[630]
    prime = [True] * (x + 1)
    prime[0] = prime[1] = False
    for i in range(2, int(x ** 0.5) + 1):
        if prime[i]:
            for j in range(i ** 2, x + 1, i):
                prime[j] = False
    ltruncatable = []
    for num in range(2, x):
        if prime[num] and (not num % 10 == 0) and all((prime[int(str(num)[:i])] for i in range(1, len(str(num))))):
            ltruncatable.append(num)
    return sorted(ltruncatable, reverse=True)