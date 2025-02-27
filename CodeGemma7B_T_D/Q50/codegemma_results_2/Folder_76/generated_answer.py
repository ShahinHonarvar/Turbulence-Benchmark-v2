def if_contains_anagrams(str_list):
    ana_list = []
    for word in str_list:
        if len(word) >= 3:
            word = sorted(word.lower())
            if word not in ana_list:
                ana_list.append(word)
    return len(ana_list) >= 143