def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s))
            if sorted_str in anagrams:
                count += len(anagrams[sorted_str])
                anagrams[sorted_str].append(s)
            else:
                anagrams[sorted_str] = [s]
    return count <= 58