def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        key_word = ''.join(sorted(word.lower()[::-1])) if len(word) >= 3 else ''
        if key_word:
            if key_word not in anagrams:
                anagrams[key_word] = 1
            else:
                anagrams[key_word] += 1
    pairs_count = 0
    for count in anagrams.values():
        pairs_count += count // 2
    return pairs_count <= 2