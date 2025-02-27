def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for word in lst:
        word = word.lower()
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    for key in anagrams:
        count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return count <= 54