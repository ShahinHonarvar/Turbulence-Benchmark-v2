def if_contains_anagrams(strings):
    anagrams = {}
    for word in strings:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    count = 0
    for words in anagrams.values():
        count += len(words) * (len(words) - 1) // 2
    return count >= 178