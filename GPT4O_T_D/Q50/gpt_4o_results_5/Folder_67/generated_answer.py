from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_characters(word):
        return ''.join(sorted(word.lower()))
    anagrams = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_word = sorted_characters(string)
            anagrams[sorted_word] += 1
    anagram_pairs = 0
    for count in anagrams.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
        if anagram_pairs >= 41:
            return True
    return False