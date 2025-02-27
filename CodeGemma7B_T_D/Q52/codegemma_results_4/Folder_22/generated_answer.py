def palindrome_of_length_n(word):
    palindromes = set()
    for i in range(len(word) - 1):
        for j in range(i + 2, len(word) + 1):
            palindrome = word[i:j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes