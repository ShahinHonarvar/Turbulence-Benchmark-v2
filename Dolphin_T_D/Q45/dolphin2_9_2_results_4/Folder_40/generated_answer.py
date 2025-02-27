def palindromes_between_indices(s):
    letters = ''
    for i in range(4, 10):
        if s[i].isalpha():
            letters += s[i].lower()
    palindrome_set = set()
    for i in range(7, len(letters) + 1):
        for j in combinations(letters, i):
            palindrome = ''.join(j)
            if palindrome == palindrome[::-1]:
                palindrome_set.add(palindrome)
    return palindrome_set