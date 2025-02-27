def if_contains_anagrams(lst):

    def count_anagrams(string):
        string = string.lower()
        return ''.join(sorted(string))
    anagrams_dict = {}
    anagrams_count = 0
    for string in lst:
        if len(string) >= 3:
            anagram = count_anagrams(string)
            if anagram in anagrams_dict:
                anagrams_dict[anagram] += 1
            else:
                anagrams_dict[anagram] = 1
    for count in anagrams_dict.values():
        anagrams_count += count * (count - 1) // 2
    return anagrams_count >= 20