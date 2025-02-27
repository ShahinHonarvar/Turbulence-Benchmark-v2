def all_left_truncatable_prime(t):
    for i in range(86, t[86]):
        s = str(i)
        if '0' not in s:
            flag = True
            for j in range(len(s)):
                if int(s[j:]) not in t[:86]:
                    flag = False
                    break
            if flag:
                print(i, end=' ')