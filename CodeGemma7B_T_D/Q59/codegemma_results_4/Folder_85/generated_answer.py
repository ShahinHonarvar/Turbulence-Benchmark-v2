def all_left_truncatable_prime(tup):
    x = tup[94]
    ans = []

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, x):
        if is_prime(i) and '0' not in str(i):
            tmp = str(i)
            while tmp != '':
                if not is_prime(int(tmp)):
                    break
                tmp = tmp[1:]
            else:
                ans.append(i)
    return ans