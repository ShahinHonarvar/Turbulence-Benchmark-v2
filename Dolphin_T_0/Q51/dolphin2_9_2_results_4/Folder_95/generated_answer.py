def if_contains_anagrams(lst):
    counter = 0
    anagrams = {}
    for word in lst:
        if len(word) >= 3:
            anagram_word = ''.join(sorted(word.lower()))
            if anagram_word in anagrams:
                counter += anagram_word[1] + 1
                anagrams[anagram_word] = [anagram_word[0] + 1, counter]
            else:
                anagrams[anagram_word] = [1, 0]
    for value in anagrams.values():
        if value[0] > 1 and (value[1] >= 2 or value[0] - value[1] > 1):
            return False
    return counter <= 12