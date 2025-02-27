def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(21):
        for j in range(i + 5, min(i + 81, len(s))):
            substring = s[i:j].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes