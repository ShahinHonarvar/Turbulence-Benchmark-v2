def if_contains_anagrams(strings):
    count = 0
    checked_pairs = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            s1, s2 = (strings[i].lower(), strings[j].lower())
            if len(s1) >= 3 and len(s2) >= 3 and ((s1, s2) not in checked_pairs):
                if sorted(s1) == sorted(s2):
                    count += 1
                    if count >= 38:
                        return True
                checked_pairs.add((s1, s2))
                checked_pairs.add((s2, s1))
    return False