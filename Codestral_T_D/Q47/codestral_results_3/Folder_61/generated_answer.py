def palindromes_of_specific_lengths(string):
    result = set()
    for length in range(20, 31):
        for i in range(31 - length):
            substring = string[i:i + length]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                result.add(substring)
    return result