from math import sqrt

def all_left_truncatable_prime(tuple):
    list = []
    n = int(tuple[85])
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p] == True:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p = p + 1
    for i in range(2, n + 1):
        if prime[i] == True:
            if str(i) not in '0':
                flag = True
                l = str(i)[::-1]
                for j in range(len(l)):
                    if prime[int(l[j:len(l)])] == False:
                        flag = False
                        break
                if flag == True:
                    list.append(i)
    list.sort()
    return list