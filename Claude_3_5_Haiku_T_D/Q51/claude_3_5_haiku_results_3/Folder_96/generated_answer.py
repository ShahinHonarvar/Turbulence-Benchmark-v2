def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                sorted_i = sorted(strings[i].lower())
                sorted_j = sorted(strings[j].lower())
                if sorted_i == sorted_j:
                    anagram_pairs += 1
                    if anagram_pairs > 2:
                        return False
    return True