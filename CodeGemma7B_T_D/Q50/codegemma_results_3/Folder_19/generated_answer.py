def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagrams:
            anagrams[sorted_word] += 1
        else:
            anagrams[sorted_word] = 1
    count = 0
    for num in anagrams.values():
        if num >= 3:
            count += num * (num - 1) // 2
    return count >= 84