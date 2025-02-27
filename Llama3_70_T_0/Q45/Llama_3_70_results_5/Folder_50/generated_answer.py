def palindromes_between_indices(s):
    s = s[4:9].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 5, len(letters) + 1):
            substring = letters[i:j]
            for k in range(len(substring)):
                palindrome = substring[:k] + substring[k:][::-1]
                if len(palindrome) >= 5:
                    palindromes.add(''.join(palindrome))
    return palindromes