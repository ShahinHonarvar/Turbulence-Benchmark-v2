def filter_chars(string):
    to_remove = set((char for idx, char in enumerate(string) if 384 <= idx <= 411 and '/' <= char <= '8'))
    return ''.join((char for char in string if char not in to_remove))