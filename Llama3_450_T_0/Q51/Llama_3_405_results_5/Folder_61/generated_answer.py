def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s))
        if sorted_str in anagrams:
            count += anagrams[sorted_str]
            anagrams[sorted_str] += 1
        else:
            anagrams[sorted_str] = 1
    return count <= 50