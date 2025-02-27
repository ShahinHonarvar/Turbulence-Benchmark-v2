def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tup):

    def check_trun(n):
        s = str(n)
        for i in range(len(s) - 1, 0, -1):
            if not is_prime(int(s[i:])):
                return False
        return True
    x = tup[96]
    li = [i for i in range(x - 1, 0, -1) if is_prime(i) and check_trun(i) and ('0' not in str(i))]
    return li