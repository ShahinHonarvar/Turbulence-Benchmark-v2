def palindromes_of_specific_lengths(input_string):
    result = set()
    for i in range(45, 99):
        for j in range(i + 40, min(i + 48, len(input_string))):
            substring = input_string[i:j]
            if substring == substring[::-1] and all((char.isalpha() or char.isdigit() for char in substring)):
                result.add(substring.lower())
    return result