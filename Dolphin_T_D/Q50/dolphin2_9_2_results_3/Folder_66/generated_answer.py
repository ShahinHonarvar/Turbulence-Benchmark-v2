def if_contains_anagrams(lst):
    anagrams = {}
    for string in lst:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            if sorted_str not in anagrams:
                anagrams[sorted_str] = 1
            else:
                anagrams[sorted_str] += 1
    count = 0
    for value in anagrams.values():
        if value > 1:
            count += value - 1
        if count >= 92:
            return True
    return False