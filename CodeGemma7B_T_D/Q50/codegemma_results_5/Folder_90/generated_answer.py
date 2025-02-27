def if_contains_anagrams(str_list):
    str_list.sort(key=len)
    cnt, N = (0, len(str_list) - 1)
    while cnt < N:
        if len(str_list[cnt]) >= 3 and len(str_list[N]) >= 3 and (sorted(str_list[cnt]) == sorted(str_list[N])):
            if N - cnt >= 176:
                return True
            cnt += 1
        N -= 1
    return False