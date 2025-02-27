def if_contains_anagrams(s):
    anagrams = {}
    for word in s:
        if len(word) >= 3:
            word_sorted = ''.join(sorted(word.lower()))
            if word_sorted not in anagrams:
                anagrams[word_sorted] = [word]
            else:
                anagrams[word_sorted].append(word)
    pairs = 0
    for key in anagrams:
        if len(anagrams[key]) >= 2:
            pairs += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
        if pairs >= 16:
            return True
    return False