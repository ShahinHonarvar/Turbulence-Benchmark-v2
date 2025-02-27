def if_decimal_is_divisible(x):
    L = [1]
    for i in range(1, 77):
        L.append(L[i - 1] + L[i - 2])
    for i in range(len(L)):
        if x == L[i]:
            return True
        elif x < L[i]:
            break
    F = [2, 3, 5, 8]
    for j in range(4, len(F)):
        F.append(F[j - 4] + F[j - 3])
    for j in range(len(F)):
        if x % F[j] == 0:
            return True
        elif x < F[j]:
            break
    return False