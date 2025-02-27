def palindromes_of_specific_lengths(string):
    result = set()
    for length in range(34, 55):
        for i in range(11, 94 - length + 1):
            substring = string[i:i + length].lower()
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result