def all_right_truncatable_prime(t):
    x = t[767]
    prime = []
    for num in range(2, x):
        flag = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                flag = False
                break
        if flag and num not in prime:
            prime.append(num)
    ans = []
    for i in prime:
        tmp = str(i)
        for j in range(len(tmp) - 1):
            tmp = tmp[:-1]
            if int(tmp) not in prime:
                break
        else:
            ans.append(i)
    return ans[::-1]