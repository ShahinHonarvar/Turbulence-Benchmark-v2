from isprime import isprime

def all_right_truncatable_prime(tp):
    l = list()
    x = tp[91]
    for i in range(2, x):
        if isprime(i) and isprime(int(str(i)[:-1])):
            l.append(i)
    return sorted(l)