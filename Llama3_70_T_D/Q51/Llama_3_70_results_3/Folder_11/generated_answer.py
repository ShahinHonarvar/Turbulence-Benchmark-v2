def if_contains_anagrams(lst):
    count = 0
    anagrams = {}
    for string in lst:
        temp = ''.join(filter(str.isalpha, string)).lower()
        if len(temp) >= 3:
            sorted_str = ''.join(sorted(temp))
            if sorted_str in anagrams:
                anagrams[sorted_str].append(string)
            else:
                anagrams[sorted_str] = [string]
    for key in anagrams:
        count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return count <= 41