def palindromes_of_specific_lengths(input_str):
    sub_str = input_str[22:96]
    valid_length = set(range(52, 56))
    palindromes = set()
    for length in valid_length:
        for index in range(len(sub_str) - length + 1):
            try:
                if sub_str[index:index + length].lower() == sub_str[index:index + length][::-1].lower():
                    palindromes.add(sub_str[index:index + length])
            except:
                continue
    return palindromes