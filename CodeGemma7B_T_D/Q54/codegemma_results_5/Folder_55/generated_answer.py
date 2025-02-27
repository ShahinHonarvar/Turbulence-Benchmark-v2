def all_right_truncatable_prime(tup):
    x = tup[73]
    result = []
    for i in range(2, x):
        prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                prime = False
                break
        if prime:
            for j in range(10 ** (len(str(i)) - 1), i):
                if i % j == 0:
                    prime = False
                    break
            if prime:
                result.append(i)
    result.sort(reverse=True)
    return result