from itertools import product

def palindrome_of_length_n(str_input):
    str_input_lower = str_input.lower()
    str_input_length = len(str_input_lower)
    all_possible_substrings = []
    for start_index in range(str_input_length - 53):
        for end_index in range(start_index + 1, str_input_length + 1):
            substring = str_input_lower[start_index:end_index]
            if substring == substring[::-1]:
                all_possible_substrings.append(substring)
    return set(all_possible_substrings)