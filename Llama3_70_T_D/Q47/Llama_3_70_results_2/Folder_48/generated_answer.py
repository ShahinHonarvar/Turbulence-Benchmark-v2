def palindromes_of_specific_lengths(string):
    start = 155
    end = 283
    min_length = 104
    max_length = 120
    result = set()
    for length in range(min_length, max_length + 1):
        for i in range(start, end - length + 1):
            substring = string[i:i + length].lower()
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result