def palindromes_of_specific_lengths(input_str):
    input_str = input_str.lower()[11:84]
    palindromes_set = set()
    for length in range(13, 67):
        for i in range(len(input_str) - length + 1):
            sub_str = input_str[i:i + length]
            if sub_str == sub_str[::-1] and sub_str.isalpha():
                palindromes_set.add(sub_str)
    return palindromes_set