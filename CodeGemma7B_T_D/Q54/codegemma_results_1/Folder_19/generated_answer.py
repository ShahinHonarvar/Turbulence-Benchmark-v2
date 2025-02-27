def all_right_truncatable_prime(p):
    result = []
    for i in range(67):
        num = p[i]
        flag = True
        for j in range(1, int(num / 2) + 1):
            if num % j == 0:
                flag = False
                break
        if flag:
            tempnum = p[i] % 10
            sort_list = []
            while tempnum >= 1:
                sort_list.append(tempnum)
                tempnum = int(tempnum / 10)
            for k in range(1, len(sort_list)):
                num2 = sort_list[k:]
                num2 = int(''.join((str(n) for n in num2)))
                flag1 = True
                for j in range(1, int(num2 / 2) + 1):
                    if num2 % j == 0:
                        flag1 = False
                        break
                if not flag1:
                    flag = False
                    break
            if flag:
                result.append(p[i])
    return sorted(result)[::-1]