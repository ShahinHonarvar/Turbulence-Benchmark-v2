def return_nth_smallest_ascii(s):
    occurrences = {char: s.count(char) for char in s if 33 <= s.index(char) <= 85}
    chars = sorted(occurrences, key=lambda x: occurrences[x])
    return chars[12] if len(chars) > 12 else 'No such character'