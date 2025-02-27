def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        string = ''.join(filter(str.isalpha, string)).lower()
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string))
            if sorted_string in anagrams:
                count += anagrams[sorted_string]
                anagrams[sorted_string] += 1
            else:
                anagrams[sorted_string] = 1
    return count <= 72