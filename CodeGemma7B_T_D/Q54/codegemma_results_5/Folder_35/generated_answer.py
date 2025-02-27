def all_right_truncatable_prime(tp):

    def prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = tp[177]
    ans = []
    for i in range(2, x):
        for j in range(1, 10 ** (len(str(i)) - 1) + 1):
            n = int(str(i)[:-j])
            if prime(n) and prime(i):
                ans.append(i)
    ans.sort()
    return ans