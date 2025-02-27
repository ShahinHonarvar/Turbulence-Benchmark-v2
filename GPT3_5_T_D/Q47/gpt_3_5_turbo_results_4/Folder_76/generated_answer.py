def palindromes_of_specific_lengths(string):
    substring = string[101:293]
    substring = substring.lower()
    palindromes = set()
    for length in range(154, 183):
        for i in range(len(substring) - length + 1):
            if substring[i:i + length] == substring[i:i + length][::-1]:
                if substring[i:i + length].isalpha():
                    palindromes.add(substring[i:i + length])
    return palindromes