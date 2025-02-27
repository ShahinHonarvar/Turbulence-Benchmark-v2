def if_contains_anagrams(str_list):
    anagrams = []
    for i in str_list:
        if len(i) >= 3:
            sorted_i = ''.join(sorted(i.lower()))
            if sorted_i in anagrams:
                continue
            for j in str_list:
                if len(j) >= 3 and sorted_i == ''.join(sorted(j.lower())) and (i != j):
                    anagrams.append(sorted_i)
                    break
    return len(anagrams) >= 5