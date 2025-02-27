def all_right_truncatable_prime(tu):
    x = tu[87]
    ans = []
    for i in range(1, x):
        breaker = False
        for j in range(1, 10):
            n = int(str(i) + str(j))
            if n % 2 == 0 or n % 3 == 0:
                breaker = True
                break
            if all((n % i != 0 for i in range(5, int(n ** 0.5) + 2, 6))):
                continue
            for k in range(j + 1, 10):
                n = int(str(i) + str(j) + str(k))
                if n % 2 == 0 or n % 3 == 0:
                    breaker = True
                    break
                if all((n % i != 0 for i in range(5, int(n ** 0.5) + 2, 6))):
                    continue
                for l in range(k + 1, 10):
                    n = int(str(i) + str(j) + str(k) + str(l))
                    if n % 2 == 0 or n % 3 == 0:
                        breaker = True
                        break
                    if all((n % i != 0 for i in range(5, int(n ** 0.5) + 2, 6))):
                        continue
                    for m in range(l + 1, 10):
                        n = int(str(i) + str(j) + str(k) + str(l) + str(m))
                        if n % 2 == 0 or n % 3 == 0:
                            breaker = True
                            break
                        if all((n % i != 0 for i in range(5, int(n ** 0.5) + 2, 6))):
                            continue
                        for n in range(m + 1, 10):
                            breaker = True
                        if breaker:
                            break
        if not breaker:
            ans.append(i)
    if not ans:
        return []
    else:
        return sorted(ans)