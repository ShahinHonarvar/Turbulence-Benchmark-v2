def if_contains_anagrams(lst):
    anagrams = {}
    cnt = 0
    for word in lst:
        w = ''.join(filter(str.isalpha, word)).lower()
        if len(w) < 3:
            continue
        sorted_word = ''.join(sorted(w))
        if sorted_word in anagrams:
            cnt += anagrams[sorted_word]
            anagrams[sorted_word] += 1
        else:
            anagrams[sorted_word] = 1
    return cnt <= 39