from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for word in strings:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagrams[sorted_word].append(word)
    count = 0
    for words in anagrams.values():
        n = len(words)
        if n > 1:
            count += n * (n - 1) // 2
            if count >= 42:
                return True
    return False