def palindromes_of_specific_lengths(string):
    specified_range = string[18:88]
    palindromes = set()
    for length in range(38, 61):
        for i in range(len(specified_range) - length + 1):
            substring = specified_range[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes