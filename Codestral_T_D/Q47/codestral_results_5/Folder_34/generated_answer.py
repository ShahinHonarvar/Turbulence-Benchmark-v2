def palindromes_of_specific_lengths(string):
    result = set()
    string = string[200:301].lower()
    for length in range(10, 51):
        for i in range(len(string) - length + 1):
            substring = string[i:i + length]
            if substring == substring[::-1]:
                result.add(substring)
    return result