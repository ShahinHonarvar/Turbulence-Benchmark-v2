def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        word_lower = word.lower()
        sorted_word = ''.join(sorted(word_lower))
        if len(word_lower) < 3 or not sorted_word.isalpha():
            continue
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word_lower)
        else:
            anagrams[sorted_word] = [word_lower]
    count = sum((1 for words in anagrams.values() if len(words) > 1))
    return count <= 19