def palindromes_of_specific_lengths(input_string):
    text = input_string[24:98]
    result = set()
    for length in range(10, 37):
        for index in range(len(text) - length + 1):
            substring = text[index:index + length]
            if all((char.isalpha() for char in substring)) and substring.lower() == substring[::-1].lower():
                result.add(substring)
    return result