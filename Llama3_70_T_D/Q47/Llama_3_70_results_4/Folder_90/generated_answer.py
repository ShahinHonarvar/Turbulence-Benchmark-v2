def palindromes_of_specific_lengths(s):
    substr = ''.join(filter(str.isalpha, s[106:281].lower()))
    palindromes = set()
    for length in range(136, 152):
        for i in range(len(substr) - length + 1):
            temp = substr[i:i + length]
            if temp == temp[::-1]:
                palindromes.add(temp)
    return palindromes