def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(17, 73):
        for j in range(i + 49, min(i + 52, len(s))):
            substring = s[i:j + 1].lower()
            if substring in palindromes or substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes