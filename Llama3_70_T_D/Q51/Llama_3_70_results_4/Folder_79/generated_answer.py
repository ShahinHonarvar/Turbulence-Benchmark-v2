def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        lower_string = string.lower()
        sorted_string = ''.join(sorted(lower_string))
        if len(lower_string) >= 3 and lower_string.isalpha():
            if sorted_string in anagrams:
                anagrams[sorted_string].append(lower_string)
            else:
                anagrams[sorted_string] = [lower_string]
    for k in anagrams:
        n = len(anagrams[k])
        count += n * (n - 1) // 2
    return count <= 173