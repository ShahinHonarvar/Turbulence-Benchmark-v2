def palindromes_of_specific_lengths(s):
    s = s[15:90].lower()
    palindromes = set()
    length = len(s)
    for length in range(40, 73):
        for i in range(length - 1, length):
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes