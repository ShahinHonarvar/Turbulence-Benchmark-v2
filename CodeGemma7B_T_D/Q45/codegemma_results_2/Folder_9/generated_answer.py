def palindromes_between_indices(word):
    palindromes = set()
    for i in range(len(word) - 6):
        for j in range(i + 7):
            palindrome = word[i:j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome.upper())
    return palindromes