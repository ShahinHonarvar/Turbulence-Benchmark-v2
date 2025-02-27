def if_contains_anagrams(lst):
    count = 0
    anagram_dict = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3 and sorted_word.isalpha():
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word] += 1
                count += anagram_dict[sorted_word] - 1
            else:
                anagram_dict[sorted_word] = 1
    return count <= 69