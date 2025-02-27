def palindromes_of_specific_lengths(string):
    result = set()
    for length in range(24, 53):
        for i in range(10, 71 - length + 1):
            substring = string[i:i + length]
            if substring.lower() == substring[::-1].lower() and substring.isalpha():
                result.add(substring)
    return result