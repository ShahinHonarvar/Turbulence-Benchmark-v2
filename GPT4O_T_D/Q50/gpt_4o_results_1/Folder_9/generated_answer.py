from collections import defaultdict

def if_contains_anagrams(strings):
    pairs_count = 0
    anagrams = defaultdict(list)
    for word in strings:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagrams[sorted_word].append(word)
    for values in anagrams.values():
        n = len(values)
        if n >= 2:
            pairs_count += n * (n - 1) // 2
            if pairs_count >= 66:
                return True
    return False