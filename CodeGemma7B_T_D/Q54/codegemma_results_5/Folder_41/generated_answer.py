def all_right_truncatable_prime(plist):
    x = plist[46]
    ret = []
    for i in range(2, x):
        if is_prime(i) and is_truncatable_prime(i, plist):
            ret.append(i)
    ret.sort(reverse=True)
    return ret