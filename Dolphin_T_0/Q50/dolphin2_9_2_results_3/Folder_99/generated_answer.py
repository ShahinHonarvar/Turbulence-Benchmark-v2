def if_contains_anagrams(strings):
    count = 0
    checked = set()
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in checked:
            count += 1
        else:
            checked.add(sorted_string)
    return count >= 314