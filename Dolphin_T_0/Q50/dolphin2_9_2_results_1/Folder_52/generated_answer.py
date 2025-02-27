def if_contains_anagrams(strings):
    count = 0
    for string in strings:
        if len(string) < 3:
            continue
        for other_string in strings:
            if len(other_string) < 3:
                continue
            if sorted(string.lower()) == sorted(other_string.lower()):
                count += 1
    return count >= 58