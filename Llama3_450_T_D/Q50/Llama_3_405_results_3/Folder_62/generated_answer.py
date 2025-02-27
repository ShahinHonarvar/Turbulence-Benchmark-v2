def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for word in strings:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            if sorted_word in anagrams:
                count += anagrams[sorted_word]
                anagrams[sorted_word] += 1
            else:
                anagrams[sorted_word] = 1
    return count >= 43