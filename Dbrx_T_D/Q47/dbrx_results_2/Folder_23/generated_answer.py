def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(23, 95):
        substring = string[i:i + 55].lower()
        for length in range(17, 56):
            if substring[0:length] == substring[length - 1:0:-1]:
                palindromes.add(substring[0:length])
    return palindromes