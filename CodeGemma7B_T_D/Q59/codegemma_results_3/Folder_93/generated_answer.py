def all_left_truncatable_prime(t):
    xx = t[11]
    all = []
    for x in range(2, xx):
        if isprime(x):
            str1 = str(x)
            if '0' not in str1:
                b = True
                for a in str1:
                    b &= isprime(int(a))
                if b:
                    all.append(x)
    return sorted(all)

def isprime(a):
    if a == 2:
        return True
    for b in range(2, a):
        if a % b == 0:
            return False
    return True