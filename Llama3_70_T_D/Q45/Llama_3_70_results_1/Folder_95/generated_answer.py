def palindromes_between_indices(s):
    s = s[7:9].lower()
    palindromes = set()
    for i in range(3, len(s) + 1):
        for j in range(len(s) - i + 1):
            substr = s[j:j + i]
            for k in range(len(substr) // 2 + 1):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    palindrome = substr[:k] + char + substr[k + len(char):]
                    if palindrome == palindrome[::-1]:
                        palindromes.add(palindrome)
    return palindromes