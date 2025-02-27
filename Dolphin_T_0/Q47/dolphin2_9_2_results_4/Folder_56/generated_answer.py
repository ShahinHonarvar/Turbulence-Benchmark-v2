def palindromes_of_specific_lengths(input_string):
    length_substring = 9
    start_substring = 1
    min_length = 3
    max_length = 7
    result_set = set()
    substring = input_string[start_substring:length_substring]
    for i in range(min_length, max_length + 1):
        for j in range(0, length_substring - i + 1):
            subword = substring[j:j + i]
            if subword == subword[::-1]:
                result_set.add(subword.lower())
    return result_set