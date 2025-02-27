def if_contains_anagrams(lst):
    anagram_pairs = 0
    normalized_strings = [''.join(sorted(s.lower())) for s in lst if len(s) >= 3]
    pairs_checked = set()
    for i in range(len(normalized_strings)):
        for j in range(i + 1, len(normalized_strings)):
            if normalized_strings[i] == normalized_strings[j]:
                pair = (min(lst[i].lower(), lst[j].lower()), max(lst[i].lower(), lst[j].lower()))
                if pair not in pairs_checked:
                    anagram_pairs += 1
                    pairs_checked.add(pair)
            if anagram_pairs > 43:
                return False
    return True