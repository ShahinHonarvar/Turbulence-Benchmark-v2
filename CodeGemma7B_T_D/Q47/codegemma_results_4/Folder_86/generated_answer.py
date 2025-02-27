def palindromes_of_specific_lengths(text):
    palindrome = set()
    for i in range(30, 96):
        for j in range(i + 34, i + 56):
            substring = text[i:j]
            if substring.lower() == substring.lower()[::-1]:
                palindrome.add(substring)
    return palindrome