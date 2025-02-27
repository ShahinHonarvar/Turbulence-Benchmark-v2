def all_left_right_truncatable_prime(x):
    if max(x) >= 999:
        print('Error: maximum input number exceeds program limitations')
        return
    result = list()
    for j in range(len(x)):
        l = str(x[j])
        if len(l) <= 2:
            if int(l) == 2 or int(l) == 3 or int(l) == 5 or (int(l) == 7):
                result.append(int(l))
                continue
            continue
        if '0' in l or int(l[0]) % 2 == 0 or int(l[-1]) % 2 == 0:
            continue
        for i in range(1, len(l) - 1):
            if int(l[i]) % 2 == 0 or int(l[i]) % 3 == 0:
                break
            elif i == len(l) - 2 and int(l[i + 1]) % 2 == 0 or int(l[i + 1]) % 3 == 0:
                continue
            num = int(l[:i + 1])
            if num % 2 == 0 and num % 3 == 0:
                continue
            for j in range(5, int(num ** 0.5) + 1, 6):
                if num % j == 0 or num % (j + 2) == 0:
                    break
            else:
                if int(l[i + 1:]) % 2 == 0 and int(l[i + 1:]) % 3 == 0:
                    continue
                num = int(l[i + 1:])
                if num % 2 == 0 and num % 3 == 0:
                    continue
                for j in range(5, int(num ** 0.5) + 1, 6):
                    if num % j == 0 or num % (j + 2) == 0:
                        break
                else:
                    result.append(num)
                    continue
    result.sort()
    return result