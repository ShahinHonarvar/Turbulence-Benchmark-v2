def if_contains_anagrams(words):

    def is_anagram(s1, s2):
        return len(s1) == len(s2) and len(s1) >= 3 and (sorted(s1.lower()) == sorted(s2.lower()))
    anagram_count = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_anagram(words[i], words[j]):
                anagram_count += 1
    return anagram_count >= 66