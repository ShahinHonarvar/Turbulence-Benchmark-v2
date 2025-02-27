def return_vowels(arg):
    vowels = 'aeiou'
    out = []
    for pos in range(4, 8):
        if arg[pos] in vowels and 'p' < arg[pos].lower() <= 'r':
            out.append(arg[pos])
    if not out:
        return []
    return out