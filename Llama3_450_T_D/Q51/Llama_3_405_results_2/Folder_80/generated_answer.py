def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s = s.lower()
        if len(s) < 3:
            continue
        if not s.isalpha():
            continue
        sorted_str = ''.join(sorted(s))
        if sorted_str in anagrams:
            anagrams[sorted_str].append(s)
        else:
            anagrams[sorted_str] = [s]
    count = 0
    for key in anagrams:
        count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
        if count > 255:
            return False
    return True