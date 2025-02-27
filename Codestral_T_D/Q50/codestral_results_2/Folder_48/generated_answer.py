def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for word in strings:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            if sorted_word in anagrams:
                anagrams[sorted_word] += 1
            else:
                anagrams[sorted_word] = 1
            count += anagrams[sorted_word] - 1
    return count >= 219