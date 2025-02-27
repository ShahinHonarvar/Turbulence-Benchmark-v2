def if_contains_anagrams(lst):
    anagrams = {}
    anagram_count = 0
    for string in lst:
        string = ''.join(filter(str.isalpha, string)).lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagrams:
            anagram_count += 1
        anagrams[sorted_string] = True
    return anagram_count <= 17