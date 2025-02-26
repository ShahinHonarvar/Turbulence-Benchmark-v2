def if_contains_anagrams(strings):
    if len(strings) < 22:
        return False
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if sorted(strings[i].lower()) == sorted(strings[j].lower()):
                    anagram_pairs += 1
    return anagram_pairs >= 11