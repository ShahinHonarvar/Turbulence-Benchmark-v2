def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(30, 47):
        for start in range(26, len(s) - length + 1):
            if s[start:start + length].lower().translate({ord(c): None for c in s[start:start + length] if c not in english_letters}):
                if s[start:start + length].lower() == s[start:start + length].lower()[::-1]:
                    palindromes.add(s[start:start + length].lower())
    return palindromes