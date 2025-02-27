def if_contains_anagrams(str_list):
    anagrams = []
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if len(str_list[i]) < 3 or len(str_list[j]) < 3:
                continue
            if str_list[i].lower() == str_list[j].lower():
                anagrams.append((str_list[i], str_list[j]))
    return len(anagrams) >= 54