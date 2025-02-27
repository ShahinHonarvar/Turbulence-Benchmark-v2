def palindromes_of_specific_lengths(text):
    text = text.lower()
    substring = text[100:201]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i, len(substring)):
            palindrome = substring[i:j + 1]
            if palindrome == palindrome[::-1] and 5 <= len(palindrome) <= 10:
                palindromes.add(palindrome)
    return palindromes