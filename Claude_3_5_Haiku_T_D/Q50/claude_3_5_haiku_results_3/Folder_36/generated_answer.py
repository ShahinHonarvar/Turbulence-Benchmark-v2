def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return len(str1) == len(str2) and len(str1) >= 3 and (sorted(str1.lower()) == sorted(str2.lower()))
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_pairs += 1
    return anagram_pairs >= 312