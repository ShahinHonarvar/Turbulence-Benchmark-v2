def palindromes_between_indices(s):
    s = s[4:10].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 5, len(letters) + 1):
            sub = letters[i:j]
            if sub == sub[::-1]:
                palindrome = ''.join(sub)
                palindromes.add(palindrome)
    return palindromes