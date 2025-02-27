def if_contains_anagrams(str_list):
    str_sets = []
    for word in str_list:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            for string_set in str_sets:
                if sorted_word in string_set:
                    string_set.add(sorted_word)
                    if len(string_set) > 3:
                        return False
            else:
                str_sets.append({sorted_word})
    return len(str_sets) <= 3