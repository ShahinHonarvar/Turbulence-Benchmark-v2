def all_left_truncatable_prime(nums):

    def isprime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    res = []
    x = nums[70]
    for i in range(2, x):
        strnum = str(i)
        if '0' not in strnum and isprime(i):
            flag = True
            for j in range(1, len(strnum)):
                if not isprime(int(strnum[j:])):
                    flag = False
                    break
            if flag:
                res.append(i)
    return sorted(res)