def all_left_truncatable_prime(n):
    x = n[784]
    result = []
    for k in range(2, x):
        if n[k] == 0:
            continue
        a = str(k)
        for j in range(len(a)):
            b = a[j:]
            if int(b) in n:
                break
        else:
            result.append(k)
    return sorted(result)