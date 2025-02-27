def if_contains_anagrams(input_list):
    anagrams = {}
    for word in input_list:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    count = 0
    for anagram_list in anagrams.values():
        if len(anagram_list) >= 3:
            count += len(anagram_list) - 2
    return count >= 46