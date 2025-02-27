def if_contains_anagrams(strings):
    anagram_count = 0
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
        length = len(anagrams[key])
        anagram_count += length * (length - 1) // 2
        if anagram_count > 93:
            return False
    return True