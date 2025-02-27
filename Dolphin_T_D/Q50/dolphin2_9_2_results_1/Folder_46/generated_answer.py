def if_contains_anagrams(words):
    anagram_pairs = list()
    for word in words:
        if len(word) < 3:
            continue
        word_sorted = ''.join(sorted(word.lower()))
        for other_word in words:
            if word == other_word or len(other_word) < 3:
                continue
            other_word_sorted = ''.join(sorted(other_word.lower()))
            if word_sorted == other_word_sorted:
                anagram_pairs.append((word, other_word))
    return len(anagram_pairs) >= 38