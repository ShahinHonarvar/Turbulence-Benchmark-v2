def all_substring_of_size_n(input_string):
    length = len(input_string)
    result = []
    for i in range(length - 2):
        substring = ''
        for j in range(i, i + 3):
            if input_string[j] in substring:
                break
            substring += input_string[j]
            if len(substring) == 3:
                result.append(substring)
    return result