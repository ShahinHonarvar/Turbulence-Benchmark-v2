def all_right_truncatable_prime(tupl):
    x = tupl[175]
    res = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            str1 = str(i)
            for k in range(1, len(str1)):
                str2 = str1[:-k]
                strint = int(str2)
                is_prime = True
                for j in range(2, strint):
                    if strint % j == 0:
                        is_prime = False
                        break
                if is_prime:
                    res.append(i)
    res = sorted(res)
    return res