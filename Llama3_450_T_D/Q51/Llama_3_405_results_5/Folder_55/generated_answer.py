def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        if len(s) >= 3 and sorted_str.isalpha():
            if sorted_str in anagrams:
                count += 1
            else:
                anagrams[sorted_str] = True
    return count <= 44