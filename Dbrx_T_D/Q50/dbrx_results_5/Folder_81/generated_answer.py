def if_contains_anagrams(strings_list):
    anagrams_count = 0
    for i in range(len(strings_list) - 1):
        string_i = strings_list[i].lower()
        if len(string_i) < 3:
            continue
        sorted_string_i = sorted(string_i)
        for j in range(i + 1, len(strings_list)):
            string_j = strings_list[j].lower()
            if len(string_j) < 3:
                continue
            if sorted(string_j) == sorted_string_i:
                anagrams_count += 1
                if anagrams_count >= 16:
                    return True
    return False