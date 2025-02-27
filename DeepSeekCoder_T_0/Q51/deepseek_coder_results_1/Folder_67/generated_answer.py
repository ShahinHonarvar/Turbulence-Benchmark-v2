def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_pairs = 0
    seen = set()
    for i, string1 in enumerate(strings):
        if len(string1) < 3:
            continue
        for j, string2 in enumerate(strings):
            if i != j and len(string2) >= 3 and ((i, j) not in seen) and ((j, i) not in seen) and is_anagram(string1, string2):
                anagram_pairs += 1
                seen.add((i, j))
                seen.add((j, i))
                if anagram_pairs > 5:
                    return False
    return anagram_pairs <= 5