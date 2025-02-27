def palindromes_of_specific_lengths(input_string):
    palindromes = set()
    length_range = range(3, 11)
    index_list = list(range(1, 300))
    for index in index_list:
        for length in length_range:
            current_substring = input_string[index - 1:index + length - 1]
            if current_substring.lower() == current_substring[::-1].lower():
                palindromes.add(current_substring)
    return palindromes