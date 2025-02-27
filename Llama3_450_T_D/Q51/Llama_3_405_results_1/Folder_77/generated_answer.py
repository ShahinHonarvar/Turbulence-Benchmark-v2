def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3 and sorted_word.isalpha():
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
    for value in anagrams.values():
        count += len(value) * (len(value) - 1) // 2
        if count > 17:
            return False
    return True