def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for word in strings:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            if sorted_word not in anagrams:
                anagrams[sorted_word] = 0
            else:
                anagrams[sorted_word] += 1
                count += anagrams[sorted_word]
    return count >= 35