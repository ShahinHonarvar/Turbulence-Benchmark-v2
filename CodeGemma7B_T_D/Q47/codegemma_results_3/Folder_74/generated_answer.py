def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[29:85]
    for i in range(len(substring) - 11):
        for j in range(i + 12, len(substring) + 1):
            subpalindrome = substring[i:j]
            if subpalindrome.isalpha():
                palindromes.add(subpalindrome)
    return palindromes