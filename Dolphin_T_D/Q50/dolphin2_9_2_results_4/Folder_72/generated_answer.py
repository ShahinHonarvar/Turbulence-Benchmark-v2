def if_contains_anagrams(lst):
    count = 0
    dic = {}
    for i in lst:
        if len(i) >= 3:
            i = i.lower()
            for j in range(len(i)):
                if sorted(i) not in dic:
                    dic[sorted(i)] = [i]
                else:
                    dic[sorted(i)].append(i)
    for k in dic.values():
        n = len(k)
        if n >= 2:
            n_tuples = n * (n - 1) // 2
            count += n_tuples
            if count >= 55:
                return True
    return False