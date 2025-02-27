def palindromes_between_indices(string):
    palindromes = set()
    for i in range(2, 7):
        for j in range(i, 7):
            palindrome = string[i:j + 1].lower()
            if palindrome == palindrome[::-1] and len(palindrome) >= 3:
                palindromes.add(palindrome)
    return palindromes