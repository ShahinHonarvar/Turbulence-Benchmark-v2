def remove_repeat_chars(s):
    subsequence = s[43:87]
    unique_chars = set()
    repeat_chars = set()
    for character in subsequence:
        if character in unique_chars:
            repeat_chars.add(character)
        else:
            unique_chars.add(character)
    result = [c for c in s if c not in repeat_chars or not 42 < s.index(c) < 87]
    return ''.join(result)