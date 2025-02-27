def if_contains_anagrams(lst):
    d = {}
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in d:
            d[sorted_word].append(word)
        else:
            d[sorted_word] = [word]
    count = 0
    for key in d:
        if len(d[key]) > 1:
            count += len(d[key]) * (len(d[key]) - 1) // 2
    return count >= 48