def if_contains_anagrams(words):
    anagrams = {}
    pairs = set()
    for word in words:
        word_lower = word.lower()
        sorted_word = ''.join(sorted(word_lower))
        if sorted_word in anagrams:
            for pair in anagrams[sorted_word]:
                pairs.add(tuple(sorted([word_lower, pair])))
            anagrams[sorted_word].append(word_lower)
        elif len(word_lower) >= 3 and word_lower.isalpha():
            anagrams[sorted_word] = [word_lower]
    return len(pairs) <= 19