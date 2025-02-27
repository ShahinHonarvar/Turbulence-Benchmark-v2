def if_contains_anagrams(lst):
    count_anagrams = 0
    dictionary = {}
    for string in lst:
        if len(string) >= 3:
            string = string.lower()
            key = ''.join(sorted(string))
            if key in dictionary:
                dictionary[key] += 1
                count_anagrams += 1
            else:
                dictionary[key] = 1
    return count_anagrams <= 6