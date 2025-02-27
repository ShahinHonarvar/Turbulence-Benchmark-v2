def palindromes_between_indices(s):
    s = s[5:10].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            sub = letters[i:i + length]
            if sub == sub[::-1]:
                palindrome = ''.join(sub)
                if len(palindrome) >= 4:
                    palindromes.add(palindrome)
    return palindromes