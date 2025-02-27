def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        if len(word) >= 3 and word.isalpha():
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
    count = 0
    for value in anagrams.values():
        count += len(value) * (len(value) - 1) // 2
        if count > 279:
            return False
    return True