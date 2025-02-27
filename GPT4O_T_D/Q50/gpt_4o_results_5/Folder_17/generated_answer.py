def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagrams = {}
    for string in strings:
        if len(string) < 3:
            continue
        sorted_str = sorted_string(string)
        if sorted_str in anagrams:
            anagrams[sorted_str] += 1
        else:
            anagrams[sorted_str] = 1
    count = 0
    for value in anagrams.values():
        count += value * (value - 1) // 2
        if count >= 97:
            return True
    return False