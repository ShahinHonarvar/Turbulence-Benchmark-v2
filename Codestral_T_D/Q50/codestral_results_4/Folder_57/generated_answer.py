def if_contains_anagrams(strings):
    count = 0
    anagrams = {}
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            if sorted_s not in anagrams:
                anagrams[sorted_s] = [s]
            else:
                anagrams[sorted_s].append(s)
                count += 1
                if count >= 50:
                    return True
    return False