def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for string in strings:
        if len(string) < 3:
            continue
        sorted_str = ''.join(sorted(string.lower()))
        if sorted_str in anagrams:
            count += len(anagrams[sorted_str])
            anagrams[sorted_str].add(string)
        else:
            anagrams[sorted_str] = {string}
    return count >= 50