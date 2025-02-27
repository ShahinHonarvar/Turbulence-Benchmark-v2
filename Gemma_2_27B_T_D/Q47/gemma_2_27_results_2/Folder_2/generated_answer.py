def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[10:60]
    for i in range(len(substring) - 17):
        for j in range(i + 18, min(i + 37, len(substring)) + 1):
            palindrome = substring[i:j]
            if palindrome.lower() == palindrome[::-1].lower() and palindrome.isalpha():
                palindromes.add(palindrome)
    return palindromes