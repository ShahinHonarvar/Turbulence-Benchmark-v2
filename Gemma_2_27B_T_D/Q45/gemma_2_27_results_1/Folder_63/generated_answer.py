def palindromes_between_indices(s):
    letters = [c for c in s[:4] if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                palindrome = ''.join(letters[i:j + 1] + letters[j:i - 1:-1])
                if len(palindrome) >= 3 and palindrome.lower() == palindrome.lower()[::-1]:
                    palindromes.add(palindrome)
    return palindromes