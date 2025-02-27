def if_contains_anagrams(strings_list):

    def get_sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagrams_count = 0
    for i in range(len(strings_list)):
        for j in range(i + 1, len(strings_list)):
            if len(strings_list[i]) >= 3 and len(strings_list[j]) >= 3 and (get_sorted_string(strings_list[i]) == get_sorted_string(strings_list[j])):
                anagrams_count += 1
    return anagrams_count <= 210