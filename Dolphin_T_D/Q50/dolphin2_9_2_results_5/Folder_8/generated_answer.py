def if_contains_anagrams(strings):
    pairs = 0
    for string1 in strings:
        if len(string1) >= 3:
            for string2 in strings:
                if string1 != string2 and len(string2) >= 3:
                    if sorted(string1.lower()) == sorted(string2.lower()):
                        pairs += 1
                        if pairs >= 85:
                            return True
    return False