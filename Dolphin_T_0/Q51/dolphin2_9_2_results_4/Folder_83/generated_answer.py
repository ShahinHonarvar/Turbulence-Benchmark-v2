def if_contains_anagrams(strings):
    pairs = 0
    checked = set()
    for string in strings:
        if len(string) >= 3 and string.lower() not in checked:
            for other_string in strings:
                if other_string == string:
                    continue
                if len(other_string) >= 3 and sorted(other_string.lower()) == sorted(string.lower()):
                    pairs += 1
                    checked.add(other_string.lower())
    return pairs <= 19