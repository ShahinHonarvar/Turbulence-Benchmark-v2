def if_contains_anagrams(lst):
    count = 0
    d = {}
    for word in lst:
        if len(word) < 3:
            continue
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if sorted_word not in d:
            d[sorted_word] = [word]
        else:
            d[sorted_word].append(word)
    for key in d:
        if len(d[key]) > 1:
            count += len(d[key]) * (len(d[key]) - 1) // 2
    return count >= 66