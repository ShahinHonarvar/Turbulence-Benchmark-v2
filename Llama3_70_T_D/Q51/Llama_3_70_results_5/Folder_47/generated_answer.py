def if_contains_anagrams(lst):
    anagram_dict = {}
    for string in lst:
        string = string.lower()
        if len(string) < 3:
            continue
        count = [0] * 26
        for char in string:
            if 'a' <= char <= 'z':
                count[ord(char) - ord('a')] += 1
        key = tuple(count)
        if key in anagram_dict:
            anagram_dict[key].append(string)
        else:
            anagram_dict[key] = [string]
    anagram_count = 0
    for key in anagram_dict:
        n = len(anagram_dict[key])
        anagram_count += n * (n - 1) // 2
    return anagram_count <= 366