def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            s1 = ''.join(sorted((c for c in strings[i].lower() if c.isalpha())))
            s2 = ''.join(sorted((c for c in strings[j].lower() if c.isalpha())))
            if len(s1) >= 3 and len(s2) >= 3 and (s1 == s2):
                count += 1
                if count > 34:
                    return False
    return True