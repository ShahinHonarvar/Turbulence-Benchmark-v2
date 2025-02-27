def all_left_truncatable_prime(t):
    x = t[14]
    i = x - 14
    plist = []
    while i > 1:
        if isprime(i) and (not '0' in str(i)):
            plist.append(i)
        i -= 1
    plist.sort(reverse=True)
    return plist