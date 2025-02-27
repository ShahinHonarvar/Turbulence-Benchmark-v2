def palindromes_between_indices(s):
    s = s[1:9].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for i in range(len(letters)):
            for j in range(i + length, len(letters) + 1):
                substring = letters[i:j]
                if substring == substring[::-1]:
                    palindrome = ''.join(substring)
                    palindromes.add(palindrome)
    return palindromes