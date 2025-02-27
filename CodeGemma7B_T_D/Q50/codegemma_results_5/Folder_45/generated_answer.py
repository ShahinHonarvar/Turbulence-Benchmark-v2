def if_contains_anagrams(words):
    seen_anagrams = set()
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            seen_anagrams.add(sorted_word)
    return len(seen_anagrams) >= 277