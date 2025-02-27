def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s = s.lower()
        if len(s) < 3:
            continue
        if not s.isalpha():
            continue
        sorted_string = ''.join(sorted(s))
        if sorted_string in anagrams:
            anagrams[sorted_string].append(s)
        else:
            anagrams[sorted_string] = [s]
    count = 0
    for value in anagrams.values():
        if len(value) > 1:
            count += len(value) * (len(value) - 1) // 2
    return count <= 61