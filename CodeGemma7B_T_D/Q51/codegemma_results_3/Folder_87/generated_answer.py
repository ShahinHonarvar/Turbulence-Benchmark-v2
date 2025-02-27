def if_contains_anagrams(str_list):
    anagrams = {}
    for word in str_list:
        if len(word) < 3 or len(set(word)) != len(word):
            continue
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word not in anagrams:
            anagrams[sorted_word] = set()
        anagrams[sorted_word].add(word)
    num_anagrams = sum((len(group) for group in anagrams.values()))
    return num_anagrams <= 392