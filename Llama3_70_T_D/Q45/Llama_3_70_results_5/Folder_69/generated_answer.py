def palindromes_between_indices(s):
    s = s[:4].lower()
    letters = [char for char in s if char.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            if letters[i] == letters[j]:
                first_half = ''.join(letters[:i] + letters[i + 1:j] + letters[j + 1:])
                for k in range(len(first_half)):
                    palindrome = letters[i] + first_half[:k] + letters[j] + first_half[k:] + letters[i]
                    if len(palindrome) >= 4:
                        palindromes.add(palindrome)
                palindrome = letters[i] + letters[j] + letters[i]
                if len(palindrome) >= 4:
                    palindromes.add(palindrome)
    return palindromes