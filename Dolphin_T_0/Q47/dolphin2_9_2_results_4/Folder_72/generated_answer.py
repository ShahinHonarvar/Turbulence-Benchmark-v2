def palindromes_of_specific_lengths(input_str):
    sub_str = input_str[25:91]
    palindromes_set = set()
    for len_ in range(27, 59):
        for index in range(0, len(sub_str) - len_ + 1):
            if sub_str[index:index + len_] == sub_str[index:index + len_][::-1].lower():
                palindromes_set.add(sub_str[index:index + len_])
    return palindromes_set