def palindromes_of_specific_lengths(input_string):
    substr = input_string[17:73].lower()
    palindromes = set()
    for length in range(50, 52):
        for start_index in range(len(substr) - length + 1):
            sub_str = substr[start_index:start_index + length]
            if sub_str == sub_str[::-1] and sub_str.isalpha():
                palindromes.add(sub_str)
    return palindromes