def if_contains_anagrams(lst):
    count = 0
    d = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            if sorted_word in d:
                count += d[sorted_word]
                d[sorted_word] += 1
            else:
                d[sorted_word] = 1
    return count >= 42