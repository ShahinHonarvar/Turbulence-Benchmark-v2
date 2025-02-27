def if_contains_anagrams(list_of_strings):
    anagram_count = 0
    sorted_strings = [''.join(sorted(s.casefold())) for s in list_of_strings if len(s) >= 3]
    for i in range(len(sorted_strings)):
        for j in range(i + 1, len(sorted_strings)):
            if sorted_strings[i] == sorted_strings[j]:
                anagram_count += 1
                if anagram_count >= 19:
                    return True
    return False