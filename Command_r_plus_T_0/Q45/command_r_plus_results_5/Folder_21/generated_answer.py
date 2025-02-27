def palindromes_between_indices(s):
    s = s[1:9].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    letters_in_s = set(s)
    if not letters_in_s.issubset(english_letters):
        return set()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            substring = s[i:j]
            if substring == substring[::-1] and len(substring) >= 7:
                palindromes.add(substring)
    return palindromes