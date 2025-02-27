def palindromes_between_indices(s):
    s = s[:5].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(len(letters)):
                if letters[i] == letters[j] and letters[i] == letters[k]:
                    palindrome = letters[i] + letters[j] + letters[k]
                    if palindrome == palindrome[::-1]:
                        palindromes.add(palindrome)
    return palindromes