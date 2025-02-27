def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        if sorted_str in anagrams:
            anagrams[sorted_str].append(s)
        else:
            anagrams[sorted_str] = [s]
    count = 0
    for value in anagrams.values():
        length = len(value)
        if length >= 2 and len(value[0]) >= 3 and value[0].isalpha():
            count += length * (length - 1) // 2
    return count <= 98