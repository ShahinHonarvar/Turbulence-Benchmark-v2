def all_right_truncatable_prime(x):
    prime = [True] * (x + 1)
    prime[0] = prime[1] = False
    for i in range(2, int(x ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, x + 1, i):
                prime[j] = False
    result = []
    for i in range(10 ** 100, x):
        if prime[i] and all((prime[int(str(i)[:-digit])] for digit in range(1, len(str(i)) + 1))):
            result.append(i)
    return sorted(result, reverse=True)