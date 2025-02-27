from collections import defaultdict

def if_contains_anagrams(strings):
    count = 0
    anagrams = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_word = ''.join(sorted(string.lower()))
            anagrams[sorted_word].append(string)
    for words in anagrams.values():
        n = len(words)
        if n > 1:
            count += n * (n - 1) // 2
            if count >= 28:
                return True
    return False