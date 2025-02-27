def palindromes_of_specific_lengths(input_str):
    input_str = input_str[:8].lower()
    palindromes = set()
    for i in range(len(input_str)):
        for j in range(i + 3, len(input_str)):
            sub_str = input_str[i:j + 1]
            if sub_str == sub_str[::-1] and 4 <= len(sub_str) <= 5 and sub_str.isalpha():
                palindromes.add(sub_str)
    return palindromes