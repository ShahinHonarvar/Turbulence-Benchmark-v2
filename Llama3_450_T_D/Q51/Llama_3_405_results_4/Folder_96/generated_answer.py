def if_contains_anagrams(string_list):
    anagrams = {}
    for s in string_list:
        sorted_str = ''.join(sorted(s.lower()))
        if len(sorted_str) >= 3 and sorted_str.isalpha():
            if sorted_str in anagrams:
                anagrams[sorted_str].append(s)
            else:
                anagrams[sorted_str] = [s]
    count = 0
    for k in anagrams:
        if len(anagrams[k]) > 1:
            count += 1
        if count > 2:
            return False
    return True