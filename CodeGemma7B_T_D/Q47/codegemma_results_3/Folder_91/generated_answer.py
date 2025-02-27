def palindromes_of_specific_lengths(input_str):
    input_str = input_str.lower()
    output_set = set()
    for i in range(0, 11):
        for j in range(i + 2, 6):
            if input_str[i:j] == input_str[j - 1:i:-1]:
                output_set.add(input_str[i:j])
    return output_set