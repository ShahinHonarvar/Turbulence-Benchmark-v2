def if_contains_anagrams(lst):
    anagrams_count = 0
    sorted_strings = [''.join(sorted(s.lower())) for s in lst if len(s) >= 3]
    for i in range(len(sorted_strings)):
        for j in range(i + 1, len(sorted_strings)):
            if sorted_strings[i] == sorted_strings[j]:
                anagrams_count += 1
                if anagrams_count >= 65:
                    return True
    return False