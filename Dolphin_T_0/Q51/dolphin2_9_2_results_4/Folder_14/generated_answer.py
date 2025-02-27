def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        if len(word) >= 3:
            key = ''.join(sorted(word.lower()))
            if key in anagrams:
                anagrams[key] += 1
            else:
                anagrams[key] = 1
    count = 0
    for key in anagrams:
        n = anagrams[key]
        pair = n * (n - 1) // 2
        count += pair
    if count > 474:
        return False
    else:
        return True