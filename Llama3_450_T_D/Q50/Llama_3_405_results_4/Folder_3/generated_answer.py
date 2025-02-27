def if_contains_anagrams(string_list):
    anagrams = {}
    count = 0
    for s in string_list:
        sorted_str = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            if sorted_str in anagrams:
                count += anagrams[sorted_str]
                anagrams[sorted_str] += 1
            else:
                anagrams[sorted_str] = 1
    return count >= 30