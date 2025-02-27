def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        lower_word = word.lower()
        if len(lower_word) >= 3:
            sorted_word = ''.join(sorted(lower_word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(lower_word)
            else:
                anagrams[sorted_word] = [lower_word]
    count = 0
    for group in anagrams.values():
        if len(group) >= 2:
            count += len(group) * (len(group) - 1) // 2
    return count >= 246