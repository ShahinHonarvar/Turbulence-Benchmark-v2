def if_contains_anagrams(str_list):
    anagrams = 0
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if sorted(''.join(sorted(str_list[i].lower()))) == sorted(''.join(sorted(str_list[j].lower()))):
                if len(str_list[i]) >= 3 and len(str_list[j]) >= 3:
                    anagrams += 1
    return anagrams <= 35