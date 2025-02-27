def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    anagrams = []
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if sorted(str_list[i]) == sorted(str_list[j]) and len(str_list[i]) >= 3 and (len(str_list[j]) >= 3):
                anagrams.append((str_list[i], str_list[j]))
    if len(anagrams) <= 318:
        return True
    else:
        return False