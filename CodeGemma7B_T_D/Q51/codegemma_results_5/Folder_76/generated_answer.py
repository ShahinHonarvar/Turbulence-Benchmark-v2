def if_contains_anagrams(str_list):
    anagrams = {}
    anagram_count = 0
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word not in anagrams:
            anagrams[sorted_word] = word
        elif anagrams[sorted_word] != word:
            anagram_count += 1
    return anagram_count <= 91