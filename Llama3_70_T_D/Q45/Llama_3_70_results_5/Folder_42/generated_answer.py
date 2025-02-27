def palindromes_between_indices(s):
    s = s[6:10].lower()
    letters = [char for char in s if char.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            palindrome = letters[i] + letters[j] + letters[i]
            if len(palindrome) >= 3:
                palindromes.add(palindrome)
            for k in range(len(letters)):
                if k != i and k != j:
                    longer_palindrome = letters[k] + palindrome + letters[k]
                    if len(longer_palindrome) >= 3:
                        palindromes.add(longer_palindrome)
    return palindromes