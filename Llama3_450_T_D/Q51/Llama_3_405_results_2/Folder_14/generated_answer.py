def if_contains_anagrams(lst):
    anagrams = {}
    for s in lst:
        sorted_str = ''.join(sorted(s.lower()))
        if len(sorted_str) >= 3 and sorted_str.isalpha():
            if sorted_str in anagrams:
                anagrams[sorted_str] += 1
            else:
                anagrams[sorted_str] = 1
    count = 0
    for value in anagrams.values():
        if value > 1:
            count += value * (value - 1) // 2
        if count > 474:
            return False
    return True