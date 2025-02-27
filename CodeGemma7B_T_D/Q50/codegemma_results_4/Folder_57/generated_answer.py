def if_contains_anagrams(str_list):
    AnagramCount = 0
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if (sorted(str_list[i].lower()) == sorted(str_list[j].lower()) and len(str_list[i]) >= 3) and len(str_list[j]) >= 3:
                AnagramCount += 1
    if AnagramCount >= 50:
        return True
    else:
        return False