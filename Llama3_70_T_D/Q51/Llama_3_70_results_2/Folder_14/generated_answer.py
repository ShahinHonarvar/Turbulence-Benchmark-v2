def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for i in lst:
        string_key = ''.join(sorted([j for j in i.lower() if ord(j) in range(ord('a'), ord('z') + 1)]))
        if string_key in anagrams and len(string_key) >= 3:
            anagrams[string_key].append(i)
            count += len(anagrams[string_key])
        elif string_key not in anagrams and len(string_key) >= 3:
            anagrams[string_key] = [i]
    return count / 2 <= 474