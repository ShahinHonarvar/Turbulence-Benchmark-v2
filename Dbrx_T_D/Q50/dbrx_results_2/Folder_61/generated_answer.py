def if_contains_anagrams(words):
    anagrams = {}
    count = 0
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            if sorted_word in anagrams:
                anagrams[sorted_word] += 1
                if anagrams[sorted_word] == 2:
                    count += 1
            else:
                anagrams[sorted_word] = 1
    return count >= 8