def all_left_truncatable_prime(t):
    x = t[92]
    l = [str(i) for i in range(2, x) if len(str(i)) > 1 and '0' not in str(i)]
    for i in l:
        if is_prime(i):
            if is_prime(i[1:]):
                for j in range(2, len(i)):
                    if not is_prime(i[j:]):
                        break
                else:
                    res.append(int(i))
    return sorted(res)