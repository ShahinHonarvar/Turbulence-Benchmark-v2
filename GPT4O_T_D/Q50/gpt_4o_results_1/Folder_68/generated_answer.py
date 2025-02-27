def if_contains_anagrams(words):

    def sorted_word(word):
        return ''.join(sorted(word.lower()))
    anagram_count = 0
    sorted_words = [sorted_word(word) for word in words if len(word) >= 3]
    word_count = {}
    for sw in sorted_words:
        if sw in word_count:
            word_count[sw] += 1
        else:
            word_count[sw] = 1
    for count in word_count.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
    return anagram_count >= 9