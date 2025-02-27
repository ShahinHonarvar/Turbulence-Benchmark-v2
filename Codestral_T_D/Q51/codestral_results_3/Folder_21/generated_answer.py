def if_contains_anagrams(strings):
    anagrams = {}
    for word in strings:
        word = word.lower()
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    for key in anagrams:
        if len(anagrams[key]) > 26:
            return False
    return True