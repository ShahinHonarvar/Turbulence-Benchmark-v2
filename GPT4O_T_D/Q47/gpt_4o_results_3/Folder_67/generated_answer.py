def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[65:100].lower()
    for length in range(26, 34):
        for start in range(0, len(substring) - length + 1):
            segment = substring[start:start + length]
            filtered_segment = ''.join(filter(str.isalpha, segment))
            if len(filtered_segment) == length and filtered_segment == filtered_segment[::-1]:
                palindromes.add(segment)
    return palindromes