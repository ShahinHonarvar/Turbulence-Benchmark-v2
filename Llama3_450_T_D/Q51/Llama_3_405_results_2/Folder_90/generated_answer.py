def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        if len(sorted_str) >= 3 and sorted_str.isalpha():
            if sorted_str in anagrams:
                anagrams[sorted_str].append(s)
            else:
                anagrams[sorted_str] = [s]
    count = 0
    for k in anagrams:
        count += len(anagrams[k]) * (len(anagrams[k]) - 1) // 2
        if count > 147:
            return False
    return True