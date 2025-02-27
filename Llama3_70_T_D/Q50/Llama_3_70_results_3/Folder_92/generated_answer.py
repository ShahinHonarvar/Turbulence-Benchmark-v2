def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for word in lst:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams and len(word) >= 3:
            anagrams[sorted_word] += 1
            if anagrams[sorted_word] == 2:
                count += 1
        elif len(word) >= 3:
            anagrams[sorted_word] = 1
    return count >= 2