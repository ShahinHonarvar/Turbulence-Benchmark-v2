from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = 0
    normalized_words = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            normalized_words[sorted_word].append(word.lower())
    for key in normalized_words:
        n = len(normalized_words[key])
        if n > 1:
            anagram_count += n * (n - 1) // 2
            if anagram_count > 72:
                return False
    return True