def if_contains_anagrams(string_list):
    anagrams = {}
    for s in string_list:
        sorted_str = ''.join(sorted(s.lower()))
        if len(s) >= 3 and sorted_str.isalpha():
            if sorted_str in anagrams:
                anagrams[sorted_str].append(s)
            else:
                anagrams[sorted_str] = [s]
    count = sum((len(val) * (len(val) - 1) // 2 for val in anagrams.values() if len(val) > 1))
    return count <= 55