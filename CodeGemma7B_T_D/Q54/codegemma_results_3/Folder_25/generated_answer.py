def all_right_truncatable_prime(a):
    x = a[92]
    a = [i for i in range(2, x) if all((not i % j for j in range(2, int(i ** 0.5) + 1)))]
    for k in range(1, len(str(x))):
        k += 1
        b = a[:]
        for j in b:
            if int(str(j)[-k:]) % k == 0:
                a.remove(j)
    return sorted(a)