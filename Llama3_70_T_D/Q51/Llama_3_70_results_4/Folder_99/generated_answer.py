def if_contains_anagrams(lst):
    anagrams_dict = {}
    for word in lst:
        word = ''.join(filter(str.isalpha, word)).lower()
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams_dict:
            anagrams_dict[sorted_word].append(word)
        else:
            anagrams_dict[sorted_word] = [word]
    anagrams_count = 0
    for words in anagrams_dict.values():
        anagrams_count += len(words) * (len(words) - 1) // 2
    return anagrams_count <= 93