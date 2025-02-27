def palindromes_of_specific_lengths(input_string):
    result = set()
    input_string = input_string.lower()
    for i in range(0, 5):
        for j in range(i, i + 3):
            if j >= len(input_string):
                break
            substring = input_string[i:j + 1]
            if substring == substring[::-1]:
                result.add(substring)
    return result