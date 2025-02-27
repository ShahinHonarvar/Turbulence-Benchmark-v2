def if_contains_anagrams(strs):
    anagrams = {}
    for word in strs:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
    count = 0
    for words in anagrams.values():
        if len(words) > 1:
            count += len(words) * (len(words) - 1) // 2
    return count >= 17