def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(s) >= 3 and sorted_s.isalpha():
            if sorted_s in anagrams:
                anagrams[sorted_s].append(s)
            else:
                anagrams[sorted_s] = [s]
    for key in anagrams:
        if len(anagrams[key]) > 1:
            count += 1
        if count > 3:
            return False
    return True