def if_contains_anagrams(s):
    anagrams = {}
    for word in s:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            sorted_word = ''.join(sorted(word_lower))
            if sorted_word in anagrams:
                anagrams[sorted_word] += 1
            else:
                anagrams[sorted_word] = 1
    for count in anagrams.values():
        if count > 255 * 2:
            return False
    return True