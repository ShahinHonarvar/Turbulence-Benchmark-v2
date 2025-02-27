def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_pairs = 0
    checked = set()
    for i, string1 in enumerate(strings):
        if len(string1) < 3:
            continue
        for j, string2 in enumerate(strings):
            if i != j and len(string2) >= 3 and ((i, j) not in checked) and ((j, i) not in checked):
                if is_anagram(string1, string2):
                    anagram_pairs += 1
                    checked.add((i, j))
                    checked.add((j, i))
                    if anagram_pairs > 3:
                        return False
    return anagram_pairs <= 3