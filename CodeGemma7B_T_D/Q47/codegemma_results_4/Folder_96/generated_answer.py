def palindromes_of_specific_lengths(string):
    lowercase_string = string.lower()
    palindromes = set()
    for i in range(100, 301):
        for j in range(50, 101):
            if i + j <= len(lowercase_string):
                substring = lowercase_string[i:i + j]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes