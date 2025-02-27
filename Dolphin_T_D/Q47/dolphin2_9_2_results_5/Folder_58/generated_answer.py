def palindromes_of_specific_lengths(string_value):
    palindromes = set()
    for length in range(109, 127):
        string_value = string_value[124:284]
        for index in range(len(string_value) - length + 1):
            if string_value[index:index + length].lower() == string_value[index:index + length].lower()[::-1] and all((c.isalpha() for c in string_value[index:index + length])):
                palindromes.add(string_value[index:index + length])
    return palindromes