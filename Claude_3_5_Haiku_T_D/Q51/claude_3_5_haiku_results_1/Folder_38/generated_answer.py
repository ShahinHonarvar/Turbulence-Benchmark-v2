def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    def is_valid_anagram(s1, s2):
        return len(s1) >= 3 and len(s2) >= 3 and is_anagram(s1, s2)
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_valid_anagram(strings[i], strings[j]):
                anagram_pairs += 1
    return anagram_pairs <= 416