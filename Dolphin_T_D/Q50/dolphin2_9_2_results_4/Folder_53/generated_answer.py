def if_contains_anagrams(lst):

    def create_sort_string(in_str):
        return ''.join(sorted(in_str.lower()))
    anagram_counter = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and (create_sort_string(lst[i]) == create_sort_string(lst[j])):
                anagram_counter += 1
                if anagram_counter >= 11:
                    return True
    return False