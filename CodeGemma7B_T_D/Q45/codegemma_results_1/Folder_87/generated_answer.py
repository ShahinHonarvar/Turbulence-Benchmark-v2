def palindromes_between_indices(text):
    text = text.lower()
    substring = text[3:10]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i, len(substring)):
            palindrome = substring[i:j + 1]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes if palindromes else set()