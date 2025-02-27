def palindromes_of_specific_lengths(s):
    s = s[200:301].lower()
    result = set()
    for start in range(len(s) - 9):
        for end in range(start + 9, min(start + 51, len(s))):
            if set(s[start:end]) <= set('abcdefghijklmnopqrstuvwxyz'):
                if s[start:end] == s[start:end][::-1]:
                    result.add(s[start:end])
    return result