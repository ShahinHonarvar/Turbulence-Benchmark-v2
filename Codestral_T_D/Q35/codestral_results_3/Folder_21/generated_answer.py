def remove_repeat_chars(s):
    chars = s[462:995]
    seen = set()
    duplicates = set((char for char in chars if char in seen or seen.add(char)))
    return ''.join((char for char in s if char not in duplicates))