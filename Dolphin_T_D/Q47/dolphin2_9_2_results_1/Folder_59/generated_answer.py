def palindromes_of_specific_lengths(string):
    substring = string[:101]
    palindromes = set()
    for length in range(3, 16):
        for i in range(0, len(substring)):
            temp = substring[i:i + length]
            if temp.lower() == temp.lower()[::-1] and temp.lower() != '':
                palindromes.add(temp)
    return palindromes