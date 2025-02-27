def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(13, 50):
        for i in range(17, 96 - length):
            substring = s[i:i + length]
            if substring.lower().encode('ascii', 'ignore').decode() == substring.lower().encode('ascii', 'ignore')[::-1].decode():
                palindromes.add(substring.lower())
    return palindromes