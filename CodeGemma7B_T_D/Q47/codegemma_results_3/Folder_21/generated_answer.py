def palindromes_of_specific_lengths(input_str):
    palindromes = set()
    input_str = input_str.lower()
    for i in range(100, 296):
        for j in range(i + 136, i + 161):
            if input_str[i:j] == input_str[j - 1:i - 1:-1]:
                palindromes.add(input_str[i:j])
    return palindromes