def if_contains_anagrams(strings):
    anagram_dict = {}
    for s in strings:
        s = s.lower()
        if len(s) < 3:
            continue
        key = ''.join(sorted(s))
        if key in anagram_dict:
            anagram_dict[key].append(s)
        else:
            anagram_dict[key] = [s]
    count = 0
    for key in anagram_dict:
        n = len(anagram_dict[key])
        count += n * (n - 1) // 2
    return count >= 177