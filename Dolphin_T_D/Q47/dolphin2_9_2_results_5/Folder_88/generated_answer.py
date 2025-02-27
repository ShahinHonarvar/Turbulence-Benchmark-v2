def palindromes_of_specific_lengths(s):
    sub_string = s[11:88]
    palindromes = set()
    for length in range(4, 6):
        for start_index in range(0, len(sub_string) - length + 1):
            sub_string_part = sub_string[start_index:start_index + length]
            if sub_string_part.lower() == sub_string_part.lower()[::-1]:
                palindromes.add(sub_string_part)
    return palindromes