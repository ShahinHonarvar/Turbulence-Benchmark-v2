def palindromes_of_specific_lengths(string):
    string = string[30:85]
    string = ''.join(filter(str.isalpha, string)).lower()
    result = set()
    for length in range(12, 21):
        for start in range(len(string) - length + 1):
            end = start + length
            substring = string[start:end]
            if substring == substring[::-1]:
                result.add(substring)
    return result