def if_contains_anagrams(lst):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    filtered_lst = [s for s in lst if len(s) >= 3]
    sorted_strings = [sort_string(s) for s in filtered_lst]
    anagram_count = 0
    for i in range(len(sorted_strings)):
        for j in range(i + 1, len(sorted_strings)):
            if sorted_strings[i] == sorted_strings[j]:
                anagram_count += 1
                if anagram_count > 97:
                    return False
    return True