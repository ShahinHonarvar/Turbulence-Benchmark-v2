from collections import defaultdict

def if_contains_anagrams(words):
    anagram_map = defaultdict(list)
    for word in words:
        cleaned_word = ''.join(filter(str.isalpha, word)).lower()
        if len(cleaned_word) >= 3:
            key = ''.join(sorted(cleaned_word))
            anagram_map[key].append(word)
    pair_count = 0
    for key in anagram_map:
        n = len(anagram_map[key])
        if n > 1:
            pair_count += n * (n - 1) // 2
            if pair_count > 11:
                return False
    return True