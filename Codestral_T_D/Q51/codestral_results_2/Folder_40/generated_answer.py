def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            if sorted_word not in anagrams:
                anagrams[sorted_word] = 1
            else:
                anagrams[sorted_word] += 1
    count = 0
    for freq in anagrams.values():
        count += freq * (freq - 1) // 2
        if count > 29:
            return False
    return True