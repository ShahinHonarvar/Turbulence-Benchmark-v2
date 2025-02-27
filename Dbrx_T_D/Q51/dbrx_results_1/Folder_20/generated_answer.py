def if_contains_anagrams(strings_list):
    anagrams_count = 0
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    for i in range(len(strings_list)):
        for j in range(i + 1, len(strings_list)):
            string_i = strings_list[i].lower()
            string_j = strings_list[j].lower()
            if len(string_i) >= 3 and len(string_j) >= 3 and (set(string_i) <= english_letters) and (set(string_j) <= english_letters) and (sorted(string_i) == sorted(string_j)):
                anagrams_count += 1
                if anagrams_count > 131:
                    return False
    return True