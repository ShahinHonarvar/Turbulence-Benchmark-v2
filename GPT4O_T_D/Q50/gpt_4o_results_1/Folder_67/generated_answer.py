from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = 0
    sorted_words = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_word = ''.join(sorted(string.lower()))
            sorted_words[sorted_word] += 1
    for count in sorted_words.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
        if anagram_count >= 41:
            return True
    return False