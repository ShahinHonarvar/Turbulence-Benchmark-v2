def all_left_truncatable_prime(_):
    x = _[37]
    trunc = ['']
    for i in range(2, x):
        if all((int(trunc[j][-1]) != 0 and all((int(trunc[j][-i]) != i for j in range(len(trunc) + 1))) for i in range(1, len(trunc[j]) + 1))):
            trunc.append(str(i))