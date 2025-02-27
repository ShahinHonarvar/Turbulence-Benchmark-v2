def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))

    def is_valid_anagram(a, b):
        return len(a) >= 3 and len(b) >= 3 and (normalize(a) == normalize(b))
    anagram_pairs = 0
    length = len(words)
    for i in range(length):
        for j in range(i + 1, length):
            if is_valid_anagram(words[i], words[j]):
                anagram_pairs += 1
                if anagram_pairs > 279:
                    return False
    return True