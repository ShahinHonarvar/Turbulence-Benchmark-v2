def if_contains_anagrams(words):
    word_count = {}
    for word in words:
        word_lower = word.lower()
        if len(word_lower) < 3:
            continue
        word_sorted = ''.join(sorted(word_lower))
        if word_sorted in word_count:
            word_count[word_sorted] += 1
        else:
            word_count[word_sorted] = 1
    anagram_count = 0
    for count in word_count.values():
        anagram_count += count * (count - 1) // 2
    return anagram_count >= 85