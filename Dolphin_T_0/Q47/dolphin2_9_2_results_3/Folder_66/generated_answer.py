def palindromes_of_specific_lengths(s):
    substring = s[32:80]
    palindromes_set = set()
    for length in range(35, 42):
        for i in range(len(substring) - length + 1):
            data = substring[i:i + length]
            if data == data[::-1] and data.isalpha():
                palindromes_set.add(data.lower())
    return palindromes_set