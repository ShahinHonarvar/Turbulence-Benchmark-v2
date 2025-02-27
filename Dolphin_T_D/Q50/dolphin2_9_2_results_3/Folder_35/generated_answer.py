def if_contains_anagrams(words):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) >= 3 and len(words[j]) >= 3 and (sort_string(words[i]) == sort_string(words[j])):
                anagram_pairs += 1
    return anagram_pairs >= 153