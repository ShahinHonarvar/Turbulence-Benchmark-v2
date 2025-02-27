def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:6] if c.isalpha()]
    palindromes = set()
    if len(letters) < 3:
        return set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                palindrome = letters[i] + letters[j] + letters[k]
                if len(palindrome) >= 3 and palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes