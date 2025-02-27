def palindromes_of_specific_lengths(s):
    sub_string = s[75:96]
    palindromes = set()
    for length in range(7, 10):
        for i in range(len(sub_string) - length + 1):
            sub_string_slice = sub_string[i:i + length]
            if sub_string_slice == sub_string_slice[::-1] and sub_string_slice.isalpha():
                palindromes.add(sub_string_slice.lower())
    return palindromes