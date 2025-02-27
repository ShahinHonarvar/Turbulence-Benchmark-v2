def palindromes_between_indices(s):
    letters = [c for c in s[7:10] if c.isalpha()]
    letters = [c.lower() for c in letters]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                palindrome = letters[i] + letters[j] + letters[k]
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes