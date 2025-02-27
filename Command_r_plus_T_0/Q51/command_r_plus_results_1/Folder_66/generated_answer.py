def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for word in lst:
        normalized = normalize(word)
        if len(word) >= 3 and normalized not in anagram_dict:
            anagram_dict[normalized] = [word]
        elif len(word) >= 3 and normalized in anagram_dict:
            anagram_dict[normalized].append(word)
    anagram_pairs = sum((1 for words in anagram_dict.values() if len(words) > 1))
    return anagram_pairs <= 64