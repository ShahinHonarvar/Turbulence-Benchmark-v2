def palindromes_of_specific_lengths(string):
    required_string = string[43:100]
    palindromes = set()
    for i in range(13, 43):
        for j in range(0, len(required_string) - i + 1):
            substring = required_string[j:j + i]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes