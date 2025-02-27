def palindrome_of_length_at_least_n(input_str):
    palindromes = set()
    input_str = input_str.lower()
    for i in range(len(input_str)):
        for j in range(i + 2, len(input_str) + 1):
            sub_str = input_str[i:j]
            if len(sub_str) >= 93 and sub_str == sub_str[::-1]:
                palindromes.add(sub_str)
    return palindromes