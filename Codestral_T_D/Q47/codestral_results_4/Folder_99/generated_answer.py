def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(119, 142):
        for i in range(127, 289 - length + 1):
            substring = s[i:i + length]
            if substring.lower() == substring[::-1].lower() and substring.isalpha():
                palindromes.add(substring)
    return palindromes