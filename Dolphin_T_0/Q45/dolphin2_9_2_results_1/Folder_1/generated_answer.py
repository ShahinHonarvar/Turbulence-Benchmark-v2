def palindromes_between_indices(string):
    letters = ''.join(sorted(set(string[4:7].lower())))
    n = len(letters)
    palindromes = set()
    for mask in range(1 << n):
        palindrome = ''
        for i in range(n):
            if mask & 1 << i:
                palindrome += letters[i]
        if len(palindrome) >= 5 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes if len(palindromes) > 0 else set()