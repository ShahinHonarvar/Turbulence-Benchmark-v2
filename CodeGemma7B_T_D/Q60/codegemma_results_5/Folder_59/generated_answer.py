from math import sqrt

def all_left_right_truncatable_prime(x):
    prime = [True for i in range(x + 1)]
    for i in range(2, int(sqrt(x)) + 1):
        if prime[i]:
            for j in range(i * i, x + 1, i):
                prime[j] = False
    result = []
    for i in range(2, x + 1):
        if prime[i]:
            str_i = str(i)
            if '0' in str_i:
                continue
            for k in range(1, len(str_i) - 1):
                a = int(str_i[:k][::-1])
                b = int(str_i[k:])
                if prime[a] and prime[b]:
                    result.append(i)
    if len(result) == 0:
        result.append(-1)
    return sorted(result, reverse=True)