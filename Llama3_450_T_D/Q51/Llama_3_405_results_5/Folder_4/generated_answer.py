def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        if sorted_str in anagrams and len(s) >= 3 and s.isalpha():
            anagrams[sorted_str].append(s)
        elif len(s) >= 3 and s.isalpha():
            anagrams[sorted_str] = [s]
    count = 0
    for value in anagrams.values():
        count += len(value) * (len(value) - 1) // 2
    return count <= 84