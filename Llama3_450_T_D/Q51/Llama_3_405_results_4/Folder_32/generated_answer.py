def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        if len(s) >= 3 and sorted_str.isalpha():
            if sorted_str in anagrams:
                anagrams[sorted_str].append(s)
            else:
                anagrams[sorted_str] = [s]
    for k in anagrams:
        if len(anagrams[k]) > 1:
            count += len(anagrams[k]) * (len(anagrams[k]) - 1) // 2
            if count > 89:
                return False
    return True