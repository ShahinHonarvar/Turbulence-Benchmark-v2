def all_substring_of_size_n(input_string):
    input_string = input_string.replace(' ', '')
    length = len(input_string)
    substrings = []
    for i in range(length):
        for j in range(i + 3, length + 1):
            substring = input_string[i:j]
            if len(substring) == 30:
                substrings.append(substring)
    substrings = set(substrings)
    result = [substring for substring in substrings if not any((substring.count(c) > 1 for c in substring))]
    return result