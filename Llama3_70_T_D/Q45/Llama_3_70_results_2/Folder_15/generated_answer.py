def palindromes_between_indices(s):
    s = s[1:3].lower()
    palindromes = set()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        for c in 'abcdefghijklmnopqrstuvwxyz':
            palindrome = char + c + char
            if set(palindrome).issubset(set(s)):
                palindromes.add(palindrome)
    return palindromes