def palindromes_between_indices(s):
    s = s[3:9].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters) + 1):
            for k in range(7 - (j - i)):
                palindrome = letters[i:j] + [''] * k + letters[i:j][::-1]
                palindromes.add(''.join(palindrome))
    return palindromes