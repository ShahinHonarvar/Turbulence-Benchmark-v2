def palindromes_of_specific_lengths(string):
    string = string[20:75].lower()
    palindromes = set()
    for length in range(36, 43):
        for i in range(len(string) - length + 1):
            if string[i:i + length] == string[i:i + length][::-1] and string[i:i + length].isalpha():
                palindromes.add(string[i:i + length])
    return palindromes