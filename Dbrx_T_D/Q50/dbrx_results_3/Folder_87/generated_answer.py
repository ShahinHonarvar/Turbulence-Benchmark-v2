def if_contains_anagrams(words):
    anagrams = {}
    count = 0
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            if sorted_word not in anagrams:
                anagrams[sorted_word] = 1
            else:
                anagrams[sorted_word] += 1
                count += 1
    if count >= 88:
        return True