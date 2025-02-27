def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_pairs = 0
    checked_indices = set()
    for i in range(len(strings)):
        if i in checked_indices:
            continue
        for j in range(i + 1, len(strings)):
            if j in checked_indices:
                continue
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and is_anagram(strings[i], strings[j]):
                anagram_pairs += 1
                checked_indices.add(i)
                checked_indices.add(j)
                if anagram_pairs > 8:
                    return False
    return anagram_pairs <= 8