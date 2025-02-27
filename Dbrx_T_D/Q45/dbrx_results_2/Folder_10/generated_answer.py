def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for start in range(len(s)):
        for end in range(start, min(len(s), start + 6)):
            substring = ''.join((c.lower() for c in s[start:end + 1] if c.lower() in english_letters))
            if len(substring) >= 3 and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes