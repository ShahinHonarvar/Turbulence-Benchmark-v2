def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[3:6].lower()))
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 4, len(letters) + 1):
            palindrome = letters[i:j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes