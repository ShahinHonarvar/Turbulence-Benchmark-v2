def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        sorted_word = ''.join(sorted([char.lower() for char in word if char.isalpha()]))
        if len(sorted_word) >= 3:
            anagrams.setdefault(sorted_word, []).append(word)
    return len(anagrams) <= 11