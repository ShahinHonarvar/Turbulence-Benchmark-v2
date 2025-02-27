def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        s_lower = s.lower()
        sorted_s = ''.join(sorted(s_lower))
        if sorted_s in anagrams and len(s_lower) >= 3 and s_lower.isalpha():
            anagrams[sorted_s].append(s_lower)
        elif len(s_lower) >= 3 and s_lower.isalpha():
            anagrams[sorted_s] = [s_lower]
    for key in anagrams:
        if len(anagrams[key]) > 1:
            count += 1
        if count > 3:
            return False
    return True