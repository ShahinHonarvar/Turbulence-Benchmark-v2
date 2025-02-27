def palindromes_of_specific_lengths(s):
    s = s[44:100]
    palindromes = set()
    for length in range(13, 43):
        for index in range(len(s) - length + 1):
            substring = s[index:index + length]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes