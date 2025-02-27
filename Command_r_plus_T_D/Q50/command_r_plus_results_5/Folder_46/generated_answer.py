def if_contains_anagrams(lst):
    anagram_count = 0
    sorted_strings = [''.join(sorted(word.lower())) for word in lst]
    for i in range(len(sorted_strings)):
        for j in range(i + 1, len(sorted_strings)):
            if sorted_strings[i] == sorted_strings[j] and len(lst[i]) >= 3 and (len(lst[j]) >= 3):
                anagram_count += 1
                if anagram_count >= 38:
                    return True
    return False