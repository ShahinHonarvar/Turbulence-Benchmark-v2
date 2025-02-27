def all_right_truncatable_prime(t):
    x = t[29]
    ans = []
    for i in range(2, x):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            flag = 1
            temp = i
            while temp > 0:
                digit = temp % 10
                temp //= 10
                if digit == 0 or (temp % (2 * digit) == 0 and temp != 0):
                    flag = 0
                    break
            if flag == 1:
                ans.append(i)
    ans.sort()
    return ans