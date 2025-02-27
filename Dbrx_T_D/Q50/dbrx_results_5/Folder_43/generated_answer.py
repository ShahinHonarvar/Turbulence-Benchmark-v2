import string

def if_contains_anagrams(list_of_strings):
    anagrams = {}
    for word in list_of_strings:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(word) >= 3:
            if sorted_word in anagrams:
                anagrams[sorted_word] += 1
            else:
                anagrams[sorted_word] = 1
    count = 0
    for value in anagrams.values():
        if value >= 2:
            count += 1 * (value * (value - 1) // 2)
    return count >= 61