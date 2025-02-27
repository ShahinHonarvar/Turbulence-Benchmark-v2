def remove_repeat_chars(s):
    seen = set()
    to_remove = set((char for char in s[86:99] if s[86:99].count(char) > 1))
    return ''.join((char for char in s if char not in to_remove))