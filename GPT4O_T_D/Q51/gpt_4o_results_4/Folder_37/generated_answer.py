def if_contains_anagrams(words):
    anagrams = {}
    count = 0
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in anagrams:
                count += anagrams[sorted_word]
                anagrams[sorted_word] += 1
            else:
                anagrams[sorted_word] = 1
            if count > 206:
                return False
    return True