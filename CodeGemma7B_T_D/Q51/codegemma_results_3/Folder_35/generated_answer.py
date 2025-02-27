def if_contains_anagrams(str_list):
    anagrams = {}
    for word in str_list:
        word = ''.join((c for c in word if c.isalpha())).lower()
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word] += 1
        else:
            anagrams[sorted_word] = 1
    return sum((count for count in anagrams.values())) <= 210