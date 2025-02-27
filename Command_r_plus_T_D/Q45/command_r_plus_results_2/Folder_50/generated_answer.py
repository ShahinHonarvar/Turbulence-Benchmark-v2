def palindromes_between_indices(s):
    letters = [c for c in s[4:9] if c.isalpha()]
    palindromes = set()
    for i in range(5, len(letters) + 1):
        for j in range(i + 1, len(letters) + 1):
            palindrome = ''.join(letters[i:j] + letters[j - 1:i - 1:-1])
            palindromes.add(palindrome.lower())
    return palindromes