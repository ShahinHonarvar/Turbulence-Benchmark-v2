def if_contains_anagrams(str):
    str_len = len(str)
    if str_len < 77:
        return False
    else:
        a = []
        for i in str:
            flag = True
            for j in str:
                if i == j:
                    continue
                a.append(i)
                if i in j or j in i:
                    flag = False
            if flag and len(i) >= 3:
                continue
            else:
                return False
        return True