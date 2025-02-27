def palindromes_between_indices(s):
    letters = ''.join((c for c in s[2:5] if c.isalpha())).lower()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            palindrome = letters[i:j] + letters[i:j][::-1]
            palindromes.add(palindrome)
    return palindromes