def all_right_truncatable_prime(tup):
    x = tup[92]
    ans = []
    for num in range(2, x + 1):
        flag = True
        for k in range(2, int(num ** 0.5) + 1):
            if num % k == 0:
                flag = False
                break
        if flag:
            while num > 0 and flag:
                flag = True
                rem = num % 10
                num //= 10
                for k in range(2, int(rem ** 0.5) + 1):
                    if rem % k == 0:
                        flag = False
                        break
            if flag and num > 0:
                ans.append(num)
    ans.sort()
    return ans