def if_contains_anagrams(string_list):
    if len(string_list) < 210:
        return False
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            if sorted(string_list[i].lower()) == sorted(string_list[j].lower()) and len(string_list[i]) >= 3:
                return True
    return False