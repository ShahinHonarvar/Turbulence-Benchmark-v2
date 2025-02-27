def palindromes_between_indices(s):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    s = s[3:6]
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            substring = s[i:j]
            lowercase_substring = ''.join((c.lower() for c in substring))
            if all((c in letters for c in lowercase_substring)) and lowercase_substring == lowercase_substring[::-1]:
                palindromes.add(substring)
    return palindromes