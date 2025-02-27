def palindromes_between_indices(s):
    s = s[1:3].lower()
    palindromes = set()
    for c in 'abcdefghijklmnopqrstuvwxyz':
        for d in 'abcdefghijklmnopqrstuvwxyz':
            palindrome = c + s + d
            if palindrome == palindrome[::-1] and len(palindrome) >= 3:
                palindromes.add(palindrome)
    return palindromes