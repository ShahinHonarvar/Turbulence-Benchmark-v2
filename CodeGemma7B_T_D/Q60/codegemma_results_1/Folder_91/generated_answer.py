def all_left_right_truncatable_prime(t):
    x = t[0]
    digs = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    results = []
    for p in range(x, 1, -1):
        if str(p)[-1] not in digs or str(p)[0] not in digs:
            continue
        if all((p % d for d in range(2, p))):
            results.append(p)
            left, right = (str(p)[1:], str(p)[:-1])
            while len(left) > 1 or len(right) > 1:
                if not all((int(left) % d for d in range(2, int(left)))):
                    break
                elif not all((int(right) % d for d in range(2, int(right)))):
                    break
                left, right = (left[1:], right[:-1])
            else:
                results.append(int(left))
                results.append(int(right))
    return sorted(results, reverse=True)