def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_count = 0
    anagram_dict = {}
    for word in words:
        if len(word) < 3:
            continue
        normalized = normalize(word)
        if normalized in anagram_dict:
            anagram_count += 1
            if anagram_count > 46:
                return False
        else:
            anagram_dict[normalized] = word
    return True