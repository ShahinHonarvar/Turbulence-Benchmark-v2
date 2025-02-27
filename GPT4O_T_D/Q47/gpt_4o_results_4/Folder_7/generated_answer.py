def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[119:257]
    filtered_string = ''.join(filter(str.isalpha, substring))
    filtered_string_lower = filtered_string.lower()
    for length in range(104, 124):
        for start in range(len(filtered_string_lower) - length + 1):
            candidate = filtered_string_lower[start:start + length]
            if candidate == candidate[::-1]:
                original_candidate = filtered_string[start:start + length]
                palindromes.add(original_candidate)
    return palindromes