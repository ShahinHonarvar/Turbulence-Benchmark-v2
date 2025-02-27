def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(10, 21):
        for index in range(10, 76 - length + 1):
            if s[index:index + length].lower() == s[index:index + length][::-1].lower():
                palindromes.add(s[index:index + length])
    return palindromes