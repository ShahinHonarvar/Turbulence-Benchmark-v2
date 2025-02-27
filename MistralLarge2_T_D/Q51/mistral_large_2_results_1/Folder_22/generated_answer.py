def if_contains_anagrams(words):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_pairs = set()
    words = [word for word in words if len(word) >= 3]
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_anagram(words[i], words[j]):
                anagram_pairs.add((min(words[i], words[j]), max(words[i], words[j])))
    return len(anagram_pairs) <= 14