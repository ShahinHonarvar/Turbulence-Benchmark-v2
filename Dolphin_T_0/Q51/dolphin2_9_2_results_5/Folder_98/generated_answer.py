def if_contains_anagrams(lst):
    count = 0
    dic = {}
    for word in lst:
        word_lower = word.lower()
        sorted_word_lower = ''.join(sorted(word_lower))
        if len(word_lower) >= 3 and sorted_word_lower in dic:
            dic[sorted_word_lower] += 1
            count += 1
        else:
            dic[sorted_word_lower] = 1
    return count <= 46