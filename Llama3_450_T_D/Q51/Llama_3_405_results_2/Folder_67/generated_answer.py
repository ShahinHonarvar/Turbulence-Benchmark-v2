def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        s = s.lower()
        if len(s) < 3 or not s.isalpha():
            continue
        key = ''.join(sorted(s))
        if key in anagrams:
            count += 1
            if count > 5:
                return False
        else:
            anagrams[key] = True
    return True