def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[4:10].lower()))
    palindromes = set()
    for i in range(5, len(letters) + 1):
        for j in range(i + 1, len(letters) + 1):
            palindrome = letters[i:j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes