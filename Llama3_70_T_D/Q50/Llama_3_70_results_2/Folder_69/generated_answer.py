def if_contains_anagrams(lst):
    anagram_dict = {}
    for string in lst:
        string = string.lower()
        if len(string) < 3:
            continue
        sorted_str = ''.join(sorted(string))
        if sorted_str in anagram_dict:
            anagram_dict[sorted_str].append(string)
        else:
            anagram_dict[sorted_str] = [string]
    count = 0
    for k in anagram_dict:
        n = len(anagram_dict[k])
        count += n * (n - 1) // 2
    return count >= 188