def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s[17:96].lower()
    for length in range(13, 50):
        for index in range(len(s) - length + 1):
            if s[index:index + length] == s[index:index + length][::-1]:
                palindromes.add(s[index:index + length])
    return palindromes