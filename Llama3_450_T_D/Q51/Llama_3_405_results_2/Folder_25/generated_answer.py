def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        if sorted_str in anagrams and len(s) >= 3 and s.isalpha():
            anagrams[sorted_str].append(s)
        elif len(s) >= 3 and s.isalpha():
            anagrams[sorted_str] = [s]
    for key in anagrams:
        if len(anagrams[key]) > 1:
            count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return count <= 67