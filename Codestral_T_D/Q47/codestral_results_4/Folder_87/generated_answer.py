def palindromes_of_specific_lengths(s):
    s = s[11:94]
    palindromes = set()
    for length in range(34, 55):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes