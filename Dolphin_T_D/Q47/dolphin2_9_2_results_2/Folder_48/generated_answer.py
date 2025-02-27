def palindromes_of_specific_lengths(s):
    substring = s[155:283 + 1]
    palindromes = set()
    for length in range(104, 121):
        for i in range(0, len(substring)):
            if substring[i:i + length].lower() == substring[i:i + length].lower()[::-1] and substring[i:i + length].isalpha():
                palindromes.add(substring[i:i + length])
    return palindromes