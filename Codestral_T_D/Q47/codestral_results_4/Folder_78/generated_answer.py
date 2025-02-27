def palindromes_of_specific_lengths(string):
    string = string[15:73]
    result = set()
    for length in range(19, 56):
        for i in range(len(string) - length + 1):
            substring = string[i:i + length]
            if substring.lower() == substring[::-1].lower() and substring.isalpha():
                result.add(substring)
    return result