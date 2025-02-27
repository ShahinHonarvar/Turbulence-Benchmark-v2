def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            if sorted_str in anagrams:
                anagrams[sorted_str] += 1
            else:
                anagrams[sorted_str] = 1
    pairs = 0
    for count in anagrams.values():
        if count > 1:
            pairs += count * (count - 1) // 2
        if pairs >= 7:
            return True
    return False