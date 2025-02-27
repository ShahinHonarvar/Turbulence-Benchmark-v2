def all_left_right_truncatable_prime(tuple1):
    num = tuple1[18]
    ans = []
    for i in range(2, num + 1):
        if str(i)[-1] in ('0', '2', '4', '5', '6', '8') or str(i)[0] in ('0', '2', '4', '5', '6', '8'):
            continue
        l_truncation = i
        r_truncation = i
        while l_truncation >= 10:
            l_truncation = int(str(l_truncation)[1:])
            r_truncation = int(str(r_truncation)[:-1])
            if str(l_truncation)[-1] in ('0', '2', '4', '5', '6', '8') or str(r_truncation)[0] in ('0', '2', '4', '5', '6', '8'):
                break
            if l_truncation not in ans and r_truncation not in ans and (l_truncation >= 2) and (r_truncation >= 2):
                ans.append(i)
    ans.sort(reverse=True)
    return ans