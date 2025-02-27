def palindromes_between_indices(s):
    letters = ''.join(sorted(s[1:7]))
    palindromes = set()
    for len_ in range(4, len(letters) + 1):
        for i in range(len(letters) - len_ + 1):
            palindrome = letters[i:i + len_]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes