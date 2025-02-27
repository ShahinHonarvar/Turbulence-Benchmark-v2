def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s = s.lower()
        if len(s) >= 3 and s.isalpha():
            sorted_str = ''.join(sorted(s))
            if sorted_str in anagrams:
                anagrams[sorted_str].append(s)
            else:
                anagrams[sorted_str] = [s]
    count = 0
    for key in anagrams:
        n = len(anagrams[key])
        if n > 1:
            count += n * (n - 1) // 2
        if count > 210:
            return False
    return True