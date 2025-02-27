def if_contains_anagrams(lst):
    anagram_dict = {}
    for string in lst:
        string = string.lower()
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string))
            if sorted_string in anagram_dict:
                anagram_dict[sorted_string].append(string)
            else:
                anagram_dict[sorted_string] = [string]
    count = 0
    for key in anagram_dict:
        n = len(anagram_dict[key])
        count += n * (n - 1) // 2
    return count >= 16