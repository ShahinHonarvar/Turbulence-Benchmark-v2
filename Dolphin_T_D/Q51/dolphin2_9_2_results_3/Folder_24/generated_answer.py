def if_contains_anagrams(list_of_strings):
    anagrams_seen = set()
    pairs = 0
    for s in list_of_strings:
        sorted_string = ''.join(sorted(s.lower())).replace(' ', '')
        if len(sorted_string) >= 3 and sorted_string in anagrams_seen:
            pairs += 1
        else:
            anagrams_seen.add(sorted_string)
    return pairs <= 96