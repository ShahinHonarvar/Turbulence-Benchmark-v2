def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            if sorted_word in anagrams:
                count += len(anagrams[sorted_word])
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
    return count >= 38