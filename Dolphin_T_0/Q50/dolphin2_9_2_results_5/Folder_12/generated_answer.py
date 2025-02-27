def if_contains_anagrams(lst):
    if len(lst) == 0:
        return False
    anagrams = {}
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word not in anagrams:
                anagrams[sorted_word] = []
            anagrams[sorted_word].append(word)
    cnt = 0
    for values in anagrams.values():
        if len(values) >= 2:
            cnt += len(values) * (len(values) - 1) // 2
            if cnt >= 69:
                return True
    return False