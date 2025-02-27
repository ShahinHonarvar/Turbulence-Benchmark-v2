def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(s) >= 3 and sorted_s.isalpha():
            if sorted_s in anagrams:
                count += 1
            else:
                anagrams[sorted_s] = True
    return count <= 15