def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        lower_word = word.lower()
        sorted_word = ''.join(sorted(lower_word))
        if len(sorted_word) < 3 or not sorted_word.isalpha():
            continue
        if sorted_word in anagrams:
            anagrams[sorted_word].append(lower_word)
        else:
            anagrams[sorted_word] = [lower_word]
    count = sum((len(words) * (len(words) - 1) // 2 for words in anagrams.values()))
    return count <= 59