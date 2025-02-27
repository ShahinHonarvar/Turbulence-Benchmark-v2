def if_contains_anagrams(lst):
    anagram_dict = {}
    count = 0
    for word in lst:
        lowercase_word = word.lower()
        sorted_word = ''.join(sorted(lowercase_word))
        if len(lowercase_word) >= 3:
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(lowercase_word)
            else:
                anagram_dict[sorted_word] = [lowercase_word]
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1:
            count += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
    return count <= 5