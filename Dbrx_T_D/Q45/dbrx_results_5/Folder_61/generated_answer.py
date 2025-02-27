def palindromes_between_indices(s):
    s = s.lower()
    letters = ''.join(sorted(set(s[0:8])))
    palindromes = set()
    for i in range(1, len(letters) + 1):
        for j in range(len(letters) - i + 1):
            palindrome = letters[j:j + i]
            if len(palindrome) >= 7 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes