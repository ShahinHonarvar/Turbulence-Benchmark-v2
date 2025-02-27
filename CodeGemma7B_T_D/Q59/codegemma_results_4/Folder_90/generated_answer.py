def all_left_truncatable_prime(n):
    left_trun = set()
    for i in range(2, n):
        l = str(i)
        if '0' not in l and len(l) > 1:
            if 'True' == all((int(l[:j]) is prime(int(l[:j])) for j in range(1, len(l)))):
                left_trun.add(i)
    return sorted(left_trun, reverse=True)

def prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True