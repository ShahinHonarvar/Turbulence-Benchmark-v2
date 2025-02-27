def if_contains_anagrams(strings):
    pairs = 0
    for i in range(len(strings)):
        lower_string = strings[i].lower()
        if len(lower_string) >= 3:
            for j in range(i + 1, len(strings)):
                lower_other_string = strings[j].lower()
                if len(lower_other_string) >= 3:
                    if sorted(lower_string) == sorted(lower_other_string):
                        pairs += 1
                        if pairs > 69:
                            return False
    return True