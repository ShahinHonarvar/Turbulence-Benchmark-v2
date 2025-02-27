from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(word1, word2):
        return sorted(word1) == sorted(word2)
    filtered_strings = [s.lower() for s in strings if len(s) >= 3]
    anagram_count = 0
    grouped = defaultdict(list)
    for word in filtered_strings:
        sorted_word = ''.join(sorted(word))
        grouped[sorted_word].append(word)
    for words in grouped.values():
        if len(words) > 1:
            anagram_count += len(words) * (len(words) - 1) // 2
            if anagram_count > 74:
                return False
    return True