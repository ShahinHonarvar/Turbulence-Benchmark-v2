def palindromes_between_indices(s):
    letters = s[6:9].lower()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            palindrome = letters[i:j + 1] + letters[j:i - 1:-1]
            if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes