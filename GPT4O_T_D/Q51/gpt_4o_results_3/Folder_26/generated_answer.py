def if_contains_anagrams(words):

    def sorted_string(s):
        return ''.join(sorted(s))
    words = [word.lower() for word in words if len(word) >= 3]
    sorted_words = [sorted_string(word) for word in words]
    anagram_pairs = 0
    for i in range(len(sorted_words) - 1):
        for j in range(i + 1, len(sorted_words)):
            if sorted_words[i] == sorted_words[j]:
                anagram_pairs += 1
                if anagram_pairs > 35:
                    return False
    return True