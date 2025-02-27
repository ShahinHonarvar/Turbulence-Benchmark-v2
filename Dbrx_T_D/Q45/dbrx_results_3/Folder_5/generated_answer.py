def palindromes_between_indices(s):
    s = s[4:9]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    if len(s) < 4:
        return palindromes
    for i in range(len(s) - 3):
        for j in range(i + 2, len(s) + 1):
            palindrome = s[i:j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes