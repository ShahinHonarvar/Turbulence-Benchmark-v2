def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in anagrams:
                anagrams[sorted_word] += 1
            else:
                anagrams[sorted_word] = 1
    count = 0
    for value in anagrams.values():
        if value > 1:
            count += value * (value - 1) // 2
        if count >= 143:
            return True
    return False