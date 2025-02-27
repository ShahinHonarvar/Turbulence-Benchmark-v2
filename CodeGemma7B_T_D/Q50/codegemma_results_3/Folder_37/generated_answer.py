def if_contains_anagrams(str_list):
    str_list.sort(key=len)
    anagrams = set()
    num_pairs = 0
    for i, str1 in enumerate(str_list):
        for j in range(i + 1, len(str_list)):
            str2 = str_list[j]
            if len(str1) not in (3, 4):
                continue
            if sorted(str1.lower()) == sorted(str2.lower()):
                num_pairs += 1
                anagrams.update({str1, str2})
    return num_pairs >= 29