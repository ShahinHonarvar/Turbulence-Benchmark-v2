def all_right_truncatable_prime(x):
    a = x[6] - 1
    b = -1
    d = {2: 0}
    p = {}
    nums = []
    for i in range(2, int(a ** 0.5) + 1):
        if d.get(i) == None:
            d[i] = 1
            for j in range(i * i, a + 1, i):
                d[j] = 0
        if d[i] == 1:
            p[i] = 1
            temp = i ** 2
            while temp <= a:
                nums.append(temp)
                temp *= i
    nums = list(set(nums))
    nums.sort(reverse=True)
    for i in range(x[6]):
        if p.get(i) == None and i in nums:
            b = i
            break
    if b == -1:
        return []
    ans = []
    for i in range(b, 0, -1):
        a = i
        c = 0
        while a != 0:
            a //= 10
            c += 1
        c -= 1
        a = i
        for k in range(c - 1, -1, -1):
            a = a % 10 ** k
            if d.get(a) == None or d[a] == 0:
                break
        if a == 0:
            ans.append(i)
    return ans