def all_left_right_truncatable_prime(A):

    def hello(A):
        s = [int(i) for i in str(A)]
        for x in range(len(s)):
            if x == len(s) - 1:
                print
            if s[0] == 0 or s[x + 1] == 0:
                return False
        return True

    def goodbye(A):
        primeList = [2]
        ind = 1
        while ind <= A:
            for x in range(2, ind):
                if ind % x == 0:
                    break
            else:
                primeList.append(ind)
            ind += 1
        return primeList

    def jonathan(A):
        p = goodbye(A)
        q = []
        for x in p:
            if hello(x):
                q.append(x)
        return q
    return jonathan(A[177])