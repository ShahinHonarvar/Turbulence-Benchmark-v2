def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_pairs = 0
    checked = []
    for i, string1 in enumerate(strings):
        if len(string1) < 3:
            continue
        for j, string2 in enumerate(strings[i + 1:], start=i + 1):
            if len(string2) < 3:
                continue
            if is_anagram(string1, string2) and (i, j) not in checked:
                anagram_pairs += 1
                checked.append((i, j))
                if anagram_pairs > 3:
                    return False
    return anagram_pairs <= 3